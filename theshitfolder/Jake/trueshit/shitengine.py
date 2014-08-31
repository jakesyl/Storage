#!/usr/bin/python
import sqlite3
import time
import datetime
conn = sqlite3.connect('database.db')
c = conn.cursor()
def engine(path, times, size):
    pathTypes =  path.split('.')
    length = len(pathTypes)
    extention = pathTypes[length-1]
    extention = (extention,)
    isin = False
    for row in c.execute('SELECT * FROM extentions WHERE ext=?', extention):
        isin = True
        if len(row) != 0:
            date = datetime.datetime.fromtimestamp(int(times)).strftime('%Y-%m-%d %H:%M:%S')
            date = date.split(" ")
            date = date[0].split("-")
            date1 = time.strftime("%d/%m/%Y")
            date1 = date1.split("/")
            if date1[1] == date[1] and date1[0] == date[0]:
                if date1[2] == date[2] or date1[2] == date[2]-1 or date1[2] == date[2]-2:
                    return False
                else:
                    return True
                else:
                return True
        else:
            return False
    if isin ==  False:
        return False