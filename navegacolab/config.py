# -*- coding: utf-8 -*-
from __future__ import print_function

import os

home = os.environ['HOME']

DEFAULT_CONFIG = {
    'paths': {
        'service_account': {
            'drive': 'Navega/NewPlatform/Config/platform-dev-service-account.json',
            'local': 'service_account.json'
        },
        'ssh_private_key': {
            'drive': 'Navega/NewPlatform/Config/ssh_private_key',
            'local': os.path.join(home, '.ssh/id_rsa')
        },
        'ssh_public_key': {
            'drive': 'Navega/NewPlatform/Config/ssh_private_key.pub',
            'local': os.path.join(home, '.ssh/id_rsa.pub')
        },
        'ssh_config': {
            'drive': 'Navega/NewPlatform/Config/ssh_config',
            'local': os.path.join(home, '.ssh/config')
        },
        'packages': {
            'drive': 'Navega/NewPlatform/Config/packages.txt',
            'local': 'packages.txt',
        }
    },
}

