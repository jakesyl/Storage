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

for user in uta:
	try:#THIS ISN'T GOING TO WORK I NEED TO LEARN MORE ABOUT HOW UBUNTU USERS WORK
		os.listdir(dirta + '/users/' + user[0])#I'm pretty sure user is still an array (inside an array)
	except OSerror:
		try c.execute()
	