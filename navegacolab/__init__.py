import os
from google.colab import auth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .drive import GDrive

DEFAULT_CONFIG = {
    'paths': {
        'service_account': {
            'drive': 'Navega/NewPlatform/Config/platform-dev-service-account.json',
            'local': 'service_account.json'
        },
        'ssh_private_key': {
            'drive': 'Navega/NewPlatform/Config/ssh_private_key',
            'local': '~/.ssh/id_rsa'
        },
        'ssh_public_key': {
            'drive': 'Navega/NewPlatform/Config/ssh_public_key.pub',
            'local': '~/.ssh/id_rsa.pub'
        }
    },
}

def init_account(config=None) 
    if config is None:
        config = DEFAULT_CONFIG
    local_path = config.get('paths').get('service_account').get('local')
    if not os.path.exists(local_path):
        auth.authenticate_user()
        drive = GDrive()
        for name in ['service_account', 'ssh_private_key', 'ssh_public_key']:
            c = config.get('paths').get(name)
            drive.download(c.get('drive'), c.get('local'))
