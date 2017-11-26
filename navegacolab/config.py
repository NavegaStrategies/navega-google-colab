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
            'drive': 'Navega/NewPlatform/Config/ssh_public_key.pub',
            'local': os.path.join(home, '.ssh/id_rsa.pub')
        }
    },
}

