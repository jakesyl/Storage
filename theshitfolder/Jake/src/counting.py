#/usr/bin/python
"""
Cortex Storage
Counts the number of files and numbers and returns the description
"""

import os
import logging
#import timeit

def counting():
	cnt_and_rd = []#Counting and Reading are defined here
	
	#Logging Setup
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)

	root=os.path.expanduser('~')

	counter =1
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
	#print i
		try:
			counter += 1#change to i+=1 later
			logger.info("Counted to file " + str(i))
			for adir in sub_dirs:
				if (adir[0]=="."):
					logger.info("We found a directory to remove!")
					fpath = adir + '/' + f
					cnt_and_rd.append(fpath)
		except BaseException:#Nothing could go wrong, right?
			logger.debug("An Error Occured, Continuing")
				continue
	cnt_and_rd.insert(1,counter)
	return cnt_and_rd #returns the count
	#stop = timeit.default_timer()
counting()#for testing