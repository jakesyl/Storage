import sqlite3# for local databases
import os#For os.walk/expand user
import logging#Avoid Printing Errors
import engine#decides wether or not a file should be uploaded
import counting#counts files to show percentage
#import upload# for uploading all our files

                                                ########BULLETIN BOARD########## 
#put shit here

#https://pythonhosted.org/pyobjc/
#We should probably catch more of this shit in the middle of the loop
# a requirements.txt doesn't seem like a bad idea
#we shouldn't keep copying and pasting logging to every new file
#WE SHOULD MAKE AN API THAT LET'S OTHER APPLICATIONS ACCESS AND UTILIZE DATA FROM OUR SQLITE3 TABLES
# WHEN YOU UPDATE THIS CODE UPDATE FROM THE BULLETIN BOARD DOWN
#blacklist these usernames https://gist.github.com/jakesyl/c1c1f24c38d6042bb04e
#Alex you need to improve performance on that time function
#WE HAVE TO IGNORE GOOGLE DRIVE AND DROPBOX AND SIMILIAR SERVICES, I already did but idk if they're right no time to test anything
#To remove .dirs make the return value an array, the first term being the int of the filecount, and the second being any .dotfiles
#Look at dependencies folder for the install order
#Alex if it's still in here remove your method for getting rid of . directories
#Percentage will not work with ignoring files, we need to figure out a way to do percentage
#Okay so the thing doesn't actually work (the script to remove, but it doesn't throw an error either so just leave it)
#note to self make the dir where the files are actually stored now called files
#Make sure that ubuntu counts memory usage frequently too
#figure out a way to get rid opf ssh

def index():
    #logging initalizing
    logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
    logger = logging.getLogger(__name__)
    count = 1#intalize completion counter 
    counterlist = counting.counting()#get's the list of dirs to be removed in addition to the number of files
    filecount = counterlist[0]#occasionally get's commented out in a commit for testing, 
    remove_dirs = ('Applications','Library','System','Developer','bin', 'cores','etc','Network','opt','private','dev', 'Google Drive', 'Dropbox')
    del counterlist[0] #removes file number
    for directory in counterlist:
        remove_dirs.append(directory)#add's directories to the remove dirs list
    conn = sqlite3.connect('database.db')#intalizing db
    conn.text_factory = unicode #what does this do?, no one knows
    c = conn.cursor()
    root=os.path.expanduser('~')#I don't know why i commented this maybe you can figure it out; change this before development
    for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
        #print '\n', dir_name
        # Make the subdirectory names stand out with / still not 100% sure what this line actually does but, hey it works right?
        #sub_dirs = [ '%s/' % n for n in sub_dirs ]
        # Mix the directory files together
          #I don't think this is neccesary at all
        files.sort()
        if (dir_name==root): #ignore these directories
            for dname in remove_dirs:
                if (dname in sub_dirs):#if dname (an item on the remove list) is a subdirectory in the current directory (in this case ~)
                    sub_dirs.remove(dname)
        for dirs in sub_dirs:
            dirs.split()
            if dirs[0] == '.':
                sub_dirs.remove(dirs)
                
        for f in files: #files represents dir_names is os.walk
            #if f in dir_name:#check if this directory shouldn't be walked
                #continue
                #Let's make sure that we don't get any .dotfiles:
            if (f[0] == '.'):
                continue
            else:
                try:
                        dbadd(conn, c, root, dir_name, sub_dirs, files, count, f, filecount)
                except OSError:
                    logger.debug("OSError, continuing")
                    continue
                except UnicodeError:
                    logger.debug("UnicodeError continuing")
                    continue
                except sqlite3.ProgrammingError:
                    logger.debug('sqlite3 error, continuing')
                    continue
            
            
    print "Complete"

def dbadd(conn, c, root, dir_name, sub_dirs, files,count,f,filecount):
    if (count==1):
        logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
        logger = logging.getLogger(__name__)
    logger.info(f + " is in " + dir_name)
    fpath = dir_name + '/' + f #used for db/by engine
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))
    count += 1.0 #Returns a float
    percentage = count/filecount
    rows = c.fetchall()

    if (len(rows)!= 0):
        c.execute ("DELETE FROM scan WHERE fpath = ?", (fpath,))#Change this when you get the chance
        
    at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
    size = os.path.getsize(os.path.join(dir_name, f))
    c.execute('INSERT INTO scan (fpath, accessDate) VALUES (?,?)', (fpath,at,))# adds files to sqlite 3 table "scan"
    boolUpload = engine.engine(fpath,at,size)#returns a value as to wether or not this file should be uploaded
    '''
    if (boolUpload == True):
        #try and catch for a shit ton of errors to (maybe)
        upload.upload(putArgsHere)
    '''
    conn.commit()#this might actually be c.commit idk what alex is doing
#index()#used for testing