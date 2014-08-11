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

uploadfile('2601:c:3480:379:aa20:66ff:fe35:3e73', 'jcortex', 'jake1998', '/home/jcortex', '/Users/Jake_Sylvestre/Documents/x.py')