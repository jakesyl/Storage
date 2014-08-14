import psycopg2 as pgsql #for postgresql interaction
import subprocess as sp#no need to type that every time?
import logging
import os#used to find out what's in a certain directory

"""

  read -p "Enter username : " username
  read -s -p "Enter password : " password
  if /usr/bin/getent passwd "$username"; then
    echo "$username exists" >&2
    exit 2
  else
    if /usr/sbin/adduser --gecos '' --disabled-password "$username"; then
      echo "User $username has been added to system"
      salt=$(echo $RANDOM | /usr/bin/md5sum | /bin/dd bs=8 count=1 2>/dev/null)
      if ! /usr/sbin/usermod --password $(/usr/bin/mkpasswd -m sha-512 "$password" "$salt") "$username"; then
         echo "Failed to set password for user $username" >&2
      fi
    else
      echo "Failed to add user $username" >&2
    fi
  fi
fi"""
sp.call("")