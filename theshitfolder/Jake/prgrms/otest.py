import os
 
for root,dirs, files in os.walk(os.path.expanduser('~')):
    print dirs
