import time # for sleeping while waiting for threads
import threading
import os
import thread #not sure if threading and thread are even the same thing, but i guess i'll find out
#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def count():
	summation = []
	fincount = 0
	root=os.path.expanduser('~')#change this before development
	print "start"
	#start = timeit.default_timer()
	dirs = os.listdir(root)
	for sub_dir in dirs:
		while (threading.activecount()>9):# if this only applies to this file, we'll keep it otherwise i have no idea what to do
				time.sleep(1)
				thread.start_new_thread(walkthedoge(sub_dir))#start a new thread for every subdir while there are less than 9 threads\
	for addable in summation:
		fincount+=addable



		#print i
		i = i+1#change to i+=1 later
	return i #returns the count
#stop = timeit.default_timer()
def walkthedoge(sub_dir,summation):
	i=0
	for dir_name, sub_dirs, files in os.walk(sub_dir):
		i+=1
	summation.append(i)		

count()# for testing remove later
#part of a subproccesss

'''
sudocode:
*find out which directories are in ~
*start a new thread for each 
*os.walk all of them
handle files using isdir
'''