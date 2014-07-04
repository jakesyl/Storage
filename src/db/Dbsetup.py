'''
Creates database and subsequent tables on users computer
'''
import sqlite3
conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()
#setting up all of the tables
#check for cluster
try:
    c.execute(''' SELECT * FROM  clusters''')
except sqlite3.OperationalError:
    #cluster
    c.execute('''CREATE TABLE clusters(id real, contents real)''')
#test for fileMap
try:
    c.execute(''' SELECT * FROM  fileMap''')
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE fileMap(path text, size text)''')
try:
    c.execute(''' SELECT * FROM  scan''')
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE scan(path text, accessDate text, accessTime text, cluster int)''')
