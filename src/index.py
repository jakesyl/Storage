import sqlite3
import os
<<<<<<< HEAD
import engine
=======
import time
import datetime
>>>>>>> FETCH_HEAD

#Table structure for future reference:     c.execute('''CREATE TABLE scan(fpath text, accessDate text)''')

conn = sqlite3.connect('database.db')#intalizing db
conn.text_factory = str #what does this do?, no one knows
c = conn.cursor()

def engine(path, times, size):
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
        print "shit5"
        return False


root='/'
def dbadd(conn, c, root, dir_name, sub_dirs, files, contents):
    print f + " is in " + dir_name
    fpath = dir_name + '/' + f
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))

    rows = c.fetchall()

    if (len(rows)!= 0):
        c.execute ("DELETE * FROM scan WHERE fpath = ?", (fpath,))# Here at cortex we don't do duplicates
        
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    size = os.path.getsize(os.path.join(dir_name, f))
    c.execute('INSERT INTO scan (fpath, accessDate) VALUES (?,?)', (fpath,at,))# adds files to sqlite 3 table "scan"
    print engine(fpath,at,size)
    conn.commit()#this might actually be c.commit idk what alex is doing

for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with / still not 100% sure what this line actually does but, hey it works right?
    #sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #I don't think this is neccesary at all
    contents.sort()
    if (dir_name==root): #ignore these directories
        sub_dirs.remove('Applications')
        sub_dirs.remove('Library')

    for f in contents:
        #if f in dir_name:#check if this directory shouldn't be walked
            #continue
        try:
                dbadd(conn, c, root, dir_name, sub_dirs, files, contents)
        except OSError:
            print "OS ERROR, I'm afraid something went wrong continuing"
            continue
        
print "complete"



'''
sudocode:
in the for loop:
go through each file
call alex's engine


'''
