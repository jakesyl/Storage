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
#cluster creation
c.execute('''CREATE TABLE clusters(id real, contents real)''')
#files
    c.execute('''CREATE TABLE fileMap(path text, cluster real, size text)''')
