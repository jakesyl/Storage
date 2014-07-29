import os
import logging
import index
import configSetup as config
import Dbsetup as makedb
import index

#Setup Logging 
logger = logging.getLogger(__name__)

contents = os.listdir(os.getcwd())#gets the contents of the current directory

if 'config.cfg' not in contents:#Makes config file if it's not there
	logger.info("No config.cfg exsist, making one")
	config.configSetup()
if 'database.db' not in contents:#build a database if it's not there	TODO I don't know if these things should be in ()
	logger.info("No database.db exsist, making one")
	makedb.makedb()

index.index()