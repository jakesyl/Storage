'''
Jake Sylvestre
Cortex Storage
Script to upload files through use of sftp
'''
import pysftp as ftp#used for server interaction through sftp
def uploadfile(ahost, ausername, apassword,remotepath,localpath):
	try:
		s = ftp.Connection(host = ahost,username= ausername, password = apassword)
		s.put(localpath,remotepath)

		s.close

	except Exception, e: # will catch later
		print str(e)

#uploadfile('localhost', 'Jake_Sylvestre', 'jake1998', 'Documents', '/Users/Jake_Sylvestre/Documents/x.py')#local ybut test