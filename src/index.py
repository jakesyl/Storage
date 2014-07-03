'''
Jake Sylvestre

'''
import os

print os.path.expanduser('~')

for root, dirs, files in os.walk(os.path.expanduser('~')):
	print root, dirs, files
	print " "


''' 
Sudocode:
Using os.walk design a for loop that starts at the root and crawls through every file 



More Details:
Dir: ~/cortexstorage/src


Other code:
1:

import os

print os.path.expanduser('~')

for root, dirs, files in os.walk(os.path.expanduser('~')):
	print root, dirs, files


2:

print "This is using getsize to see how much every file consumes"
print "---------------"
from os.path import join, getsize
for root, dirs, files in os.walk('~'):
    print root, "consumes",
    print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"
'''
