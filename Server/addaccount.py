import psycopg2 as pgsql #for postgresql interaction
import subprocess as sp#no need to type that every time?
import logging
import os#used to find out what's in a certain directory
'''
Database structure:
CREATE TABLE users(username text, tableadress int,userpath)
CREATE TABLE newusers(username text)
'''

dirta = os.path.expanduser('~') #dirta = dir to add

#logging setup
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

try:
	conn = pgsql.connect("dbname='users' user='postgres' host='localhost' password='jake1998'")
except:
    logger.info("I am unable to connect to the database")

c = conn.cursor()#We have to define a connection cursor in order to execute commands

c.execute("""SELECT * FROM newusers""")
uta = c.fetchall()#uta = users to add

userlist = sp.call("cut -d: -f1 /etc/passwd")

for user in uta:
	if user not in userlist:#just making sure we don't overwrite someone elses stuff
