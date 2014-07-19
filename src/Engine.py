import sqlite3
import time
import datetime
conn = sqlite3.connect('db/database.db')
c = conn.cursor()
def engine(path, times, size):
    for row in c.execute('SELECT * FROM extentions WHERE ext = "mp4"'):
        if len(row) != 0:
            print "shit"
    #getting file etentions
    pathTypes =  path.split('.')
    length = len(pathTypes)
    extention = pathTypes[length-1]
    extention = (extention,)
    print extention
    isin = False
    #checks for proper extetion
    for row in c.execute('SELECT * FROM extentions WHERE ext=?', extention):
        isin = True
        print row
        if len(row) != 0:
            # get readable date from file
            date = datetime.datetime.fromtimestamp(int(times)).strftime('%Y-%m-%d %H:%M:%S')
            date = date.split(" ")
            date = date[0].split("-")
            # get current time
            date1 = time.strftime("%d/%m/%Y")
            date1 = date1.split("/")
            #check if it is within the month
            if date1[1] == date[1] and date1[0] == date[0]:
                #check if it is withn the last two days
                if date1[2] == date[2] or date1[2] == date[2]-1 or date1[2] == date[2]-2:
                    #if so dont upload
                    print"shit3"
                    return False
                #if not dont upload
                else:
                    print "shit2"
                    return True
                #if not within the month no need to check just upload
            else:
                print "shit1"
                return True
            #if not proper extention dont upload
        else:
            print "shit"
            return False
    if isin ==  False:
        return False



