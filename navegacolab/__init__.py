import os
from google.colab import auth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .drive import GDrive


def init_account(drive_path, local_path='service_account.json'):
    if not os.path.exists(local_path):
        auth.authenticate_user()
        drive = GDrive()
        drive.download(drive_path, local_path)
