import sqlite3
import os
import engine
import counting
#first we should os.walk everything just for a counter so we can do file x/y uploaded
# we should increase and decrease threads dynamically based on cpu usage, not quite sure how we can do this but i found a good python c bridge:
#https://pythonhosted.org/pyobjc/

count = 1
filecount = counting.counting()
conn = sqlite3.connect('database.db')#intalizing db
conn.text_factory = unicode #what does this do?, no one knows
c = conn.cursor()
root=os.path.expanduser('~')#I don't know why i commented this maybe you can figure it out; change this before development
print root
remove_dirs = ('Applications','Library','System','Developer','bin', 'cores','etc','Network','opt','private','dev')

def dbadd(conn, c, root, dir_name, sub_dirs, files, contents):
    print f + " is in " + dir_name
    fpath = dir_name + '/' + f
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))
    count +=1
    percentage = count/filecount
    rows = c.fetchall()

    if (len(rows)!= 0):
        c.execute ("DELETE FROM scan WHERE fpath = ?", (fpath,))# Here at cortex we don't do duplicates
        
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    size = os.path.getsize(os.path.join(dir_name, f))
    c.execute('INSERT INTO scan (fpath, accessDate) VALUES (?,?)', (fpath,at,))# adds files to sqlite 3 table "scan"
    engine.engine(fpath,at,size)
    conn.commit()#this might actually be c.commit idk what alex is doing

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


