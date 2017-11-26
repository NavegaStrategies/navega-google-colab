import os
from google.colab import auth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from .config import DEFAULT_CONFIG
from .drive import GDrive


def init_account(config=None, user_email=None):
    if config is None:
        config = DEFAULT_CONFIG
    if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
        auth.authenticate_user()
    drive = GDrive(user_email=user_email)
    for name in ['service_account', 'ssh_private_key', 'ssh_public_key', 'ssh_config']:
        c = config.get('paths').get(name)
        drive.download(c.get('drive'), c.get('local'))
