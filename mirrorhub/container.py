"""Submodule of mirrorhub.

provides methods to initialize the mirror container.
"""
import os
import signal
from subprocess import Popen
from jinja2 import Template
from mirrorhub.utils import exec_cmd


LETSENCRYPT_ARGS = ' '.join(['-a webroot',
                             '--webroot-path=/tmp/letsencrypt',
                             '--rsa-key-size 4096',
                             '--non-interactive'])
PATHS = {'letsencrypt': '',
         'dhparams': '/srv/nginx/dhparam.pem',
         'templates': '/srv/internals/',
         'rsync': '/etc/rsyncd.conf',
         'nginx': {'s-a': '/etc/nginx/sites-available/mirror.conf',
                   's-e': '/etc/nginx/sites-enabled/mirror.conf'}}


def sslcert_exists():
    """Check whether a ssl certificate already exists.

    Args:
        domain (str): mirror domain
    Returns:
        bool: check result
    """
    return os.path.exists(os.path.join([PATHS['letsencrypt'], 'live', '']))


def dhparams_exists():
    """Check whether dhparams already exists.

    Returns:
        bool: check result
    """
    return os.path.isfile(PATHS['dhparams'])


def build_nginx_conf(temp_name, domain, service):
    """Build the nginx config out of the given template.

    Args:
        temp_name (str): name of the jinja2 based template file
        domain (str): mirror domain
        service (str): name of the mirrored service
    """
    template = Template(open(PATHS['templates'] + temp_name + '.j2').read())
    with open(PATHS['nginx']['s-a'], 'w+') as file_:
        file_.write(template.render(domain=domain, mirror_name=service))
    if os.path.isfile(PATHS['nginx']['s-e']):
        os.unlink(PATHS['nginx']['s-e'])
    os.symlink(PATHS['nginx']['s-a'], PATHS['nginx']['s-e'])


def build_rsync_conf(service):
    """Build the rsync config out of the given template.

    Args:
        service (str): name of the mirrored service
    """
    template = Template(open(PATHS['templates']).read())
    with open(PATHS['rsync'], 'w+') as file_:
        file_.write(template.render(mirror_name=service))


def create_sslcert(domain, service):
    """Create a letsencrypt ssl certificate.

    Args:
        domain (str): mirror domain
        service (str): name of the mirrored service
    """
    build_nginx_conf('mirror_nonssl', domain, service)
    nginx = Popen('/usr/sbin/nginx')
    exec_cmd('letsencrypt certonly %s --register-unsafely-without-email \
             --agree-tos -d %s' % (LETSENCRYPT_ARGS, domain))
    os.kill(nginx.pid, signal.SIGTERM)


def renew_sslcert():
    """Renew an existing letsencrypt ssl certificate."""
    exec_cmd('letsencrypt renew ' + LETSENCRYPT_ARGS)


def run_supervisor():
    """Run the supervisord in the docker container."""
    exec_cmd('/usr/bin/supervisord')
