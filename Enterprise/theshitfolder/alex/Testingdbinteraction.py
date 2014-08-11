import sqlite3
conn = sqlite3.connect('db/database.db')#intalizing db
c = conn.cursor()

for row in c.execute('SELECT * FROM scan):
        print row
