import os
import logging
import index
import Dbsetup as makedb
import index

#Setup Logging 
logger = logging.getLogger(__name__)

#contents = os.listdir(os.getcwd())#gets the contents of the current directory

makedb.makedb()#not dependent on wether or not there is actually a database
index.index()