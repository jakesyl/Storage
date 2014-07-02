'''
Creates database and subsequent tables on users computer
'''
import sqlite3
conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()
#setting up all of the tables
#cluster creation
c.execute('''CREATE TABLE clusters(id real, contents real)''')
#files
c.execute('''CREATE TABLE fileMap(path text, cluster real, size text)''')
