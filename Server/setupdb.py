import psycopg2 as pgsql #for postgresql interaction
import logging

#logging setup
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

try:
	conn = pgsql.connect("dbname='users' user='postgres' host='localhost' password='pass'")
except:
    logger.info("I am unable to connect to the database")

c = conn.cursor()#We have to define a connection cursor in order to execute commands


try:
	('''SELECT * FROM  users''')
except:
	c.execute('''CREATE TABLE users(username text, tableadress int,userpath text)''')
	logger.info("Table filemap doesn't exsist creating it")

try:
	('''SELECT * FROM  newusers''')
except:
	c.execute('''CREATE TABLE newusers(username text)''')
	logger.info("Table newusers doesn't exsist creating it")
