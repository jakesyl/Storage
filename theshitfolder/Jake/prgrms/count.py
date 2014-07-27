import threading
import os
import thread #not sure if threading and thread are even the same thing, but i guess i'll find out
#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def count():
	summation = ()
	root=os.path.expanduser('~')#change this before development
	print "start"
	#start = timeit.default_timer()
	dirs = os.listdir(root)
			for sub_dir in dirs:
				if (threading.activecount()<9):# if this only applies to this file, we'll keep it otherwise i have no idea what to do
					thread.start_new_thread(walkthedoge(sub_dir))
					#array .append the output of the thread i think i'm still not really sure how threading in python works



		#print i
		i = i+1#change to i+=1 later
	return i #returns the count
#stop = timeit.default_timer()
count()
def walkthedoge(sub_dir,summation):
	i=0
	for dir_name, sub_dirs, files in os.walk(sub_dir):
		i = i + 1 #shouldn't this be i+=1



#part of a subproccesss

'''
sudocode:
*find out which directories are in ~
*start a new thread for each 
*os.walk all of them
handle files using isdir
'''