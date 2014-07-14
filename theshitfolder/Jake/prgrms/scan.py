import sqlite3
import os

conn = sqlite3.connect('database.db')#intalizing db
conn.text_factory = str #what does this do?, no one knows
c = conn.cursor()
# If we are not given a path to list, use /tmp
root='/'
def dbadd(conn, c, root, dir_name, sub_dirs, files, contents):
    print f + " is in " + dir_name
    fpath = dir_name + '/' + f
    c.execute ("SELECT * FROM clusters WHERE contents = ?", (fpath,))
    #c.execute('SELECT * FROM clusters WHERE contents = '+ path);
    clustery = c.fetchone()
    if clustery is None:
        cluster = "undefined"
    else:
        cluster = clustery[0]
    cluster = "undefined" #if undefined alex will find it
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    c.execute('INSERT INTO scan (fpath, accessDate, cluster) VALUES (?,?,?)', (fpath,at, cluster,))

for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #originally sub_dirs + files
    contents.sort()
    for f in contents:
        if f in excludes:#check if this directory shouldn't be walked
            continue
        try:
            dbadd(conn, c, root, dir_name, sub_dirs, files, contents)
        except OSError:
            print "ERROR ERROR TERROR BE WARRIE"
            continue
        
print "complete"

'''
output:

ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.
'''
