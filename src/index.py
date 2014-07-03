'''
Jake Sylvestre

'''
import os

for root, dirs, files in os.walk(os.path.expanduser('~')):
	#print root #just prints the directory it's in
 	

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
'''
