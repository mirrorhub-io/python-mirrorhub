#!/usr/bin/env python3
"""Init script which prepares our docker container."""
import os
from mirrorhub import LOGO
from mirrorhub import container as ct
from mirrorhub.api import APIClient

api_client = APIClient(os.getenv('CLIENT_TOKEN'))
data = api_client.get_mirror_info()
DOMAIN = data['domain']
SERVICE = data['service']['name']

print(LOGO)

if ct.dhparams_exists():
    print('[nginx] Using existing dhparams')
else:
    print('[nginx] Did not found dhparams, generating.\
           This may take a while..')
    ct.create_dhparams()
    print('[nginx] Finished generating.')

if ct.sslcert_exists(DOMAIN):
    print('[cert] Found certificate for domain. Attempt renew..')
    ct.renew_sslcert()
else:
    print('[cert] Missing certificate for domain. Request new one..')
    ct.create_sslcert(DOMAIN, SERVICE)


print('[nginx] Applying final site configuration..')
ct.build_nginx_conf('mirror', DOMAIN, SERVICE)

print('[rsync] Building rsync configuration..')
ct.build_rsync_conf(SERVICE)

print('[mirror] Ready to serve!')
ct.run_supervisor()
