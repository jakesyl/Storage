import sqlite3
import time
from time import strftime
from datetime import datetime
conn = sqlite3.connect('/db/database.db')
c = conn.cursor()
def engine(path, time, size):
    pathTypes =  path.split('.')
    length = len(pathTypes)
    print length
    extention = pathTypes[length-1]
    extention = (extention, )
    print extention
    for row in c.execute('SELECT * FROM extentions WHERE ext=?,',extention)
    if len(row) != 0:
        date = datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
        date = date.split(" ")
        date = date[0].split("-")
        timestamp = int(time.time())
        date1 = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        date1 = date.split(" ")
        date1 = date[0].split("-")
        





engine("downloads/shit/tile.txt", "time", 100003)
