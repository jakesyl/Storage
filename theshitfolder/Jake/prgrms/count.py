import os
#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def count():
	i=1 #fuck naming conventions
	root=os.path.expanduser('~')#change this before development
	print "start"
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
		#print i
		i = i+1#change to i+=1 later
	return i #returns the count
#stop = timeit.default_timer()

'''
Note this might already be fixed (i'm rerunning)

TODO fix this error:
Traceback (most recent call last):
  File "count.py", line 12, in <module>
    stop = timeit.default_timer()
TypeError: cannot concatenate 'str' and 'int' objects


'''