#!/usr/bin/env python3
"""Init script which prepares our docker container."""
from mirrorhub import LOGO
from mirrorhub import container as ct


print(LOGO)

if ct.dhparams_exists():
    print('[nginx] Using existing dhparams')
else:
    print('[nginx] Did not found dhparams, generating.\
           This may take a while..')
    ct.create_dhparams()
    print('[nginx] Finished generating.')

print('[nginx] Using %s as HOSTNAME' % ct.HOSTNAME)

if ct.sslcert_exists():
    print('[cert] Found certificate for domain. Attempt renew..')
    ct.renew_sslcert()
else:
    print('[cert] Missing certificate for domain. Request new one..')
    ct.create_sslcert()


print('[nginx] Applying final site configuration..')
ct.build_nginx_conf('mirror')

print('[rsync] Building rsync configuration..')
ct.build_rsync_conf()

print('[mirror] Ready to serve!')
ct.run_supervisor()
