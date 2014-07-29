import os
import logging


#import timeit
#TODO add a shit ton more threads
#just counts files were indexing
def counting():
	#Log Here
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)
	
	root=os.path.expanduser('~')#change this before development
	#print "start"
	i=1
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
		#print i
		try:
			i = i+1#change to i+=1 later
			logger.info("Counted to file " + str(i))
		except BaseException:#Nothing could go wrong, right?
			logger.debug("An Error Occured, Continuing")
			continue 
	return i #returns the count
	#stop = timeit.default_timer()