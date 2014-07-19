import sqlite3
import time
from time import strftime
from datetime import datetime
conn = sqlite3.connect('db/database.db')
c = conn.cursor()
def engine(path, time, size):
    #getting file etentions
    pathTypes =  path.split('.')
    length = len(pathTypes)
    print length
    extention = pathTypes[length-1]
    extention = (extention, )
    print extention
    #checks for proper extetion
    for row in c.execute('SELECT * FROM extentions WHERE ext=?',extention):
        if len(row) != 0:
            # get readable date from file
            date = datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
            date = date.split(" ")
            date = date[0].split("-")
            # get current timestamp
            timestamp = int(time.time())
            #get date from current
            date1 = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            date1 = date.split(" ")
            date1 = date[0].split("-")
            #check if it is within the month
            if date1[1] == date[1] and date1[0] == date[0]:
                #check if it is withn the last two days
                if date1[2] == date[2] or date1[2] == date[2]-1 or date1[2] == date[2]-2:
                    #if so dont upload
                    return False
                #if not dont upload
                else:
                    return True
                #if not within the month no need to check just upload
            else:
                return True
            #if not proper extention dont upload
        else:
            return False
        





print engine("downloads/shit/tile.txt", 1405738428, 10003)
