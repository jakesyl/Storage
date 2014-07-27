import os
import timeit
#TODO add a shit ton more threads
#just counts files were indexing
i=1 #fuck naming conventions
root=os.path.expanduser('~')#change this before development
print "start"
start = timeit.default_timer()
for dir_name, sub_dirs, files in os.walk(root):
	#print i
	i = i+1#change to i+=1 later
stop = timeit.default_timer()
print "i is " + str(i)
print "done"
print stop - start #runtime
'''
Note this might already be fixed (i'm rerunning)

TODO fix this error:
Traceback (most recent call last):
  File "count.py", line 12, in <module>
    stop = timeit.default_timer()
TypeError: cannot concatenate 'str' and 'int' objects


'''