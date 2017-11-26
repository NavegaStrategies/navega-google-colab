import os
from google.colab import auth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .drive import GDrive


def get_service_account(drive_path, local_path='service_account.json'):
    if not os.path.exists(local_path):
        auth.authenticate_user()
        drive = GDrive()
        drive_id, fname, folder_id = drive.path_to_id(drive_path)
        service_account_file = drive.CreateFile({'id': drive_id})
        service_account_file.GetContentFile(local_path)
