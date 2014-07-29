import sqlite3
import os
import engine
import counting
#https://pythonhosted.org/pyobjc/ what were using for objective C in cocoa, note for ALEX
#TODO get rid of contents, just not quite ready to do this in vim

count=1 #Increments every time a file is fully scanned/ (if needed) uploaded NOT FOR COUNT
filecount = counting.counting()#Counts files in order to show a percentage
conn = sqlite3.connect('database.db')#intalizing db
conn.text_factory = unicode #May delete later, not sure if this actually does anything
c = conn.cursor()
root=os.path.expanduser('~')
print root
remove_dirs = ('Applications','Library','System','Developer','bin', 'cores','etc','Network','opt','private','dev')

def dbadd(conn, c, root, dir_name, sub_dirs, files, contents, count):
    print f + " is in " + dir_name
    fpath = dir_name + '/' + f
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))
    count +=1# increment count for percentage showing
    percentage = count/filecount#Get percentage
    rows = c.fetchall()

    if (len(rows)!= 0):
        c.execute ("DELETE FROM scan WHERE fpath = ?", (fpath,))#Deletes duplicates in scan TODO fix this to store history
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    size = os.path.getsize(os.path.join(dir_name, f))
    c.execute('INSERT INTO scan (fpath, accessDate) VALUES (?,?)', (fpath,at,))#adds files to sqlite 3 table "scan"
    engine.engine(fpath,at,size)# Returns true or false as to wether or not to upload
    conn.commit()

for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with / still not 100% sure what this line actually does but, hey it works right?
    #sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #I don't think this is neccesary at all
    contents.sort()
    if (dir_name==root): #ignore these directories
        for dname in remove_dirs:
            if (dname in sub_dirs):#if dname (an item on the remove list) is a subdirectory in the current directory (in this case ~)
                sub_dirs.remove(dname)
    for dirs in sub_dirs:
        dirs.split()
        if dirs[0] == '.':
            sub_dirs.remove(dirs)
            
    for f in contents: #contents represents dir_names is os.walk
        #if f in dir_name:#check if this directory shouldn't be walked
            #continue
        try:
                dbadd(conn, c, root, dir_name, sub_dirs, files, contents,count)
        except OSError:
            print "OS ERROR, I'm afraid something went wrong continuing"
            continue
        except UnicodeError:
            print "UnicodeError continuing"
            continue
        except sqlite3.ProgrammingError:
            print 'sqlite3 error'
            continue
        
        
print "complete"


