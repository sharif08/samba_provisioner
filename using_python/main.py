from os import path
from dotenv import load_dotenv
load_dotenv()
import sys
import os
import base64
import subprocess

def mount_function(smb_user, smb_pass, smb_domain, path_to_smb):

  # Decrypt the password
  password_d = base64.b64decode(smb_pass).decode('utf-8')


  # Mount the samba
  retcode = subprocess.call(["/sbin/mount", "-t", "cifs", "-o credentials=/.smb_credentials", "//HostName.LOCAL/MSSQLSERVER", "/app/smbconfig/smbmount"])

  # Remove the file
  os.remove(".smb_credentials")

# 1. Main
if __name__=='__main__':
    smb_user          =  os.getenv('server_user')
    smb_pass          =  os.getenv('server_pass')
    smb_domain        =  os.getenv('server_domain')
    mount_function(smb_user, smb_pass, smb_domain, path_to_smb)
