import threading
import os
#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def count():
	thrad_count = 1 #not using thread.active count because i'm not sure how localized that is...
	i=1 #fuck naming conventions
	root=os.path.expanduser('~')#change this before development
	print "start"
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
		while (dir_name==root):
			for sub_dirs in dir_name:
				if (thread_count)

		#print i
		i = i+1#change to i+=1 later
	return i #returns the count
#stop = timeit.default_timer()
count()
def 


'''
sudocode:
*find out which files are in ~
*start a new thread for each 