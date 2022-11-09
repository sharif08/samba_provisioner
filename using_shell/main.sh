#!/bin/bash

# Version 1.0

# ENVs
source .env

echo "start script"

# Decrypt the password
d_password=$(echo $server_pass | base64 --decode)

# Mount the samba
DIR="/app/smbmount"

if [ -d "$DIR" ]; then
  mount -t cifs -o username=$server_user,password=$d_password,domain=$server_domain \
  //HOSTName.LOCAL/MSSQLSERVER /app/smbmount
else
  echo "DIR not fount /app/smbmount"
fi

echo "end script"
