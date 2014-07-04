import os

conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()

# If we are not given a path to list, use /tmp
root='/'
for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #originally sub_dirs + files
    contents.sort()
    for f in contents:
        print f + " is in " + dir_name
        c.execute('''commands''')#put something that's not retarted here

