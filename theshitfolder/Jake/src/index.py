#!/usr/bin/python

'''
Cortex Storage
Determines wether or not a file should be uploaded by means of time
'''

import sqlite3# for local databases
import os#For os.walk/expand user
import logging#Avoid Printing Errors
import engine#decides wether or not a file should be uploaded
import counting#counts files to show percentage
#import upload# for uploading all our files

def index():
    #Sets up Logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    count = 1#intalize completion counter
    counterlist = counting.counting()#Get directories to remove/file count
    filecount = counterlist[0] #file count is [0] else is dir to remove
    remove_dirs = []
    del counterlist[0] #removes file number
    for directory in counterlist:
        remove_dirs.append(directory)#add's directories to the remove dirs list
    conn = sqlite3.connect('database.db')#intalizing db
    conn.text_factory = unicode #what does this do?, no one knows
    c = conn.cursor()
    root=os.path.expanduser('~')#Start at userdir
    for dir_name, sub_dirs, files in os.walk(root):
        files.sort()
        if (dir_name==root): #ignore these directories
            for dname in remove_dirs:
                if (dname in sub_dirs):
                    sub_dirs.remove(dname)
        for dirs in sub_dirs:
            dirs.split()
            if dirs[0] == '.':
                sub_dirs.remove(dirs)

        for f in files: #files are dir_names
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

def dbadd(conn, c, root, dir_name, sub_dirs, files,count,f,filecount):
    if (count==1):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
    logger.info(f + " is in " + dir_name)
    fpath = dir_name + '/' + f #used for db/by engine
    c.execute ("SELECT * FROM scan WHERE fpath = ?", (fpath,))
    count += 1.0 #Returns a float
    percentage = count/filecount
    rows = c.fetchall()

    if (len(rows)!= 0):
        c.execute ("DELETE FROM scan WHERE fpath = ?", (fpath,))

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
index()#used for testing