'''
Jake Sylvestre

'''
import sqllite
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
        #print f + " is in " + dir_name
        path = dir_name + '/' + f
        clustery = c.execute('SELECT * FROM clusters WHERE contents = '+ path);
        if (clustery === 'NULL'):
            cluster = "undefined" #if undefined alex will find it
        at=os.path.getatime(os.sep.join(dir_name, f]))#last access time of file
        c.execute('INSERT INTO scan (fpath, accessDate, cluster)]  VALUES ('fpath, at, cluster);')'#put something that is not retarted here
 

	'''
Sudocode:
Using os.walk design a for loop that starts at the root and crawls through every file 



More Details:
Dir: ~/cortexstorage/src

other code:
import os

print os.path.expanduser('~')

for root, dirs, files in os.walk(os.path.expanduser('~')):# for every root in 
	print root, dirs, files
	print " "

Explanation for above code:
root :	Prints out directories only from what you specified
dirs :	Prints out sub-directories from root. 
files:  Prints out all files from root and directories

old useless code: # If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    for c in contents:
        print '\t%s' % c


'''