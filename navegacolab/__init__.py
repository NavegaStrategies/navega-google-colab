# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import shlex
import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from .config import DEFAULT_CONFIG
from .drive import GDrive


def init(config=None, user_email=None, verbose=False):
    from google.colab import auth
    if config is None:
        config = DEFAULT_CONFIG
    sc_local = config.get('paths').get('service_account').get('local')
    if not os.path.exists(sc_local) and os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
        auth.authenticate_user()
    drive = GDrive(user_email=user_email)
    for name in ['service_account', 'ssh_private_key', 'ssh_public_key', 'ssh_config', 'packages']:
        c = config.get('paths').get(name)
        drive.download(c.get('drive'), c.get('local'))
    os.chmod(config.get('paths').get('ssh_private_key').get('local'), 0600)
    for n, v in config.get('envs').items():
        os.environ[n] = v
    pkg_local = config.get('paths').get('packages').get('local')
    with open(pkg_local, 'r') as f:
        for name in f:
            name = name.strip()
            print('Install', name)
            cmd = 'pip install --no-cache-dir --upgrade {1} {0}'.format(name, '--queit' if not verbose else '')
            args = shlex.split(cmd)
            subprocess.check_call(args)

