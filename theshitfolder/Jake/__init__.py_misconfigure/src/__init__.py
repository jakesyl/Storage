"""
Jake Sylvestre
The purpose of this file is to import other files and start a main.py
"""
import sqlite3# for local databases
import os#For os.walk/expand user
import logging#Avoid Printing Errors
import time# for engine analysis
import datetime#for engine analysis/timestamp reading
import ConfigParser#for Alex's config file
import engine#decides wether or not a file should be uploaded
import counting#counts files to show percentage
import main as indexerMain#indexes files, starts everything else
import paramiko#For ssh interaction for file uploads
import upload# uploads files
import fileReplace#replaces files, TODO use this import
import Dbsetup as makedb#Sets up Database
import counting#sets up counting
import configSetup as config#sets up the config file

contents = os.listdir(os.getcwd())#gets the contents of the current directory

if 'configfile' not in contents:#Makes config file if it's not there
	config.configSetup()

if 'database.db' not in contents:#build a database if it's not there	TODO I don't know if these things should be in ()
	makedb.makedb()

indexerMain.index()