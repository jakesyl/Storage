import sqlite3
import os

conn = sqlite3.connect('database.db')#intalizing db
conn.text_factory = str #what does this do?, no one knows
c = conn.cursor()
root='/'
def dbadd(conn, c, root, dir_name, sub_dirs, files, contents):
    print f + " is in " + dir_name
    fpath = dir_name + '/' + f
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))
    
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    c.execute('INSERT INTO scan (fpath, accessDate) VALUES (?,?)', (fpath,at, cluster,))# adds files to sqlite 3 table "scan"

for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with / still not 100% sure what this line actually does but, hey it works right?
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #I don't think this is neccesary at all
    contents.sort()
    #if (dir_name==root): # this isn't working quite right, please come back later!!
        #sub_dirs.remove('Applications')#same here

    for f in contents:
        #if f in dir_name:#check if this directory shouldn't be walked
            #continue
        try:
                dbadd(conn, c, root, dir_name, sub_dirs, files, contents)
        except OSError:
            print "ERROR ERROR TERROR BE WARRIE"
            continue
        
print "complete"


