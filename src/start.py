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

makedb.makedb()#not dependent on wether or not there is actually a database
index.index()