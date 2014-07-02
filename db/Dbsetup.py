import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
#setting up all of the tables
#clusters
c.execute('''CREATE TABLE clusters(id real, contents real)''')
#files
c.execute('''CREATE TABLE fileMap(path text, cluster real)''')
