import os
import logging


#import timeit
#just counts files were indexing in addition to making a list of directories to remove
def counting():
	cnt_and_rd = []
	#Log Here
	logging.basicConfig(level=logging.INFO)#We should be setting this elsewhere
	logger = logging.getLogger(__name__)

	root=os.path.expanduser('~')#change this before development
	#print "start"
	count = 1
	#start = timeit.default_timer()
	for dir_name, sub_dirs, files in os.walk(root):
		#print i
		try:
			count += 1#change to i+=1 later
			logger.info("Counted to file " + str(count))
			for adir in sub_dirs:
				if (adir[0]=="."):
					logger.info("We found a directory to remove!")
					fpath = adir + '/' + f#adds dir path
					cnt_and_rd.append(fpath)
		except BaseException:#Nothing could go wrong, right?
			logger.debug("An Error Occured, Continuing")
			continue
	cnt_and_rd.insert(1,count)
	return cnt_and_rd #returns the count
	#stop = timeit.default_timer()
#counting()#for testing
