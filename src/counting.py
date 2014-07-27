import os
#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def counting():
	root=os.path.expanduser('~')#change this before development
	#print "start"
	i=1
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
		#print i
		i = i+1#change to i+=1 later
		print "I counted to file " + str(i)
	return i #returns the count
	#stop = timeit.default_timer()