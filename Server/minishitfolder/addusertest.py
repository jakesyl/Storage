import psycopg2 as pgsql #for postgresql interaction
import subprocess as sp#no need to type that every time?
import logging
import os#used to find out what's in a certain directory

sp.call("#!/bin/bash","if [ $(id -u) -eq 0 ]; then","	read -p \"Enter username : \" username", 	"read -s -p \"Enter password : \" password","	egrep \"^$username\" /etc/passwd >/dev/null", "	if [ $? -eq 0 ]; then ", "echo \"$username exists!", 'exit 1','	else', '		pass=$(perl -e \'print crypt($ARGV[0], "password")\' $password)', '	fi', 'else','	echo "Only root may add a user to the system"', 	'exit 2', 'fi')