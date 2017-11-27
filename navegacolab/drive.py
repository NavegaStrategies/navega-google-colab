# -*- coding: utf-8 -*-
from __future__ import print_function

import os
from oauth2client.client import GoogleCredentials 
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from .config import DEFAULT_CONFIG


class GDrive(object):
    def __init__(self, gauth=None, user_email=None, config=None):
        if config is None:
            config = DEFAULT_CONFIG
        if gauth is None:
            gauth = GoogleAuth()
            scred = None
            service_account_local = config.get('paths').get('service_account').get('local')
            if os.path.exists(service_account_local):
                scopes = ['https://www.googleapis.com/auth/drive']
                scred = ServiceAccountCredentials.from_json_keyfile_name(
                            service_account_local,
                            scopes=scopes)
                scred = scred.create_delegated(sub=user_email)
            else:
                scred = GoogleCredentials.get_application_default()
            gauth.credentials = scred
        self.drive = GoogleDrive(gauth)
    
    def folder_to_id(self, path):
        path_comp = path.split('/')
        parent_id = 'root'
        for comp in path_comp:
            q = "'{parent_id}' in parents and title='{comp}' and trashed=false".format(parent_id=parent_id, comp=comp)
            #print(parent_id, comp, q)
            l = self.drive.ListFile({'q': q}).GetList()
            if l:
                parent_id = l[0]['id']
            else:
                raise AttributeError('No such folder')
        return parent_id
    
    def dir(self, path):
        if path == '/':
            q = "'root' in parents and trashed=false"
        else:
            fid = self.folder_to_id(path)
            q = "'{folder_id}' in parents and trashed=false".format(folder_id=fid)
        return self.drive.ListFile({'q': q}).GetList()

    def download(self, drive_path, local_path):
        drive_id, fname, folder_id = self.path_to_id(drive_path)
        f = self.drive.CreateFile({'id': drive_id})
        return f.GetContentFile(local_path)
    
    def path_to_id(self, path):
        folder_name, file_name = os.path.dirname(path), os.path.basename(path)
        folder_id = self.folder_to_id(folder_name)
  
        q = "'{folder_id}' in parents and title='{name}' and trashed=false".format(folder_id=folder_id, name=file_name)
        l = self.drive.ListFile({'q': q}).GetList()
        if l:
            return l[0]['id'], file_name, folder_id
        return None, file_name, folder_id
