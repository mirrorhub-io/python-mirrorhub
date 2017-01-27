'''submodule if mirrorhub, which provides method to initialize the mirror container'''
import os
import signal
import socket
from subprocess import Popen
from jinja2 import Template

from mirrorhub.utils import exec_cmd

HOSTNAME = socket.gethostname()
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
    '''check whether a ssl certificate already exists
    returns:
        bool: check result'''
    return os.path.exists(os.path.join([PATHS['letsencrypt'], 'live', '']))

def dhparams_exists():
    '''check whether dhparams already exists
    returns:
        bool: check result'''
    return os.path.isfile(PATHS['dhparams'])
