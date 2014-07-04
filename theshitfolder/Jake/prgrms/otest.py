import os

for root,dirs, files in os.walk(os.path.expanduser('~')):
    #values test
    print "root directory is"+"and in this directory there are " + root + "roots and " + files "files"
