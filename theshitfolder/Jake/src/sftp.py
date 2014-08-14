'''
Jake Sylvestre
Cortex Storage
Script to upload files through use of sftp
'''
import pysftp as ftp#used for server interaction through sftp
def uploadfile(ahost, ausername, apassword,aremotepath,localpath):
	s = ftp.Connection(host = ahost,username= ausername, password = apassword)
	ftp.cd(aremotepath)
	s.put(localpath,preserve_mtime=True)
	s.close

uploadfile('2601:c:3480:379:c523:346c:2c10:59aa', 'jcortex', 'jake1998', '/home/jcortex/cortexstorage', '/Users/Jake_Sylvestre/Documents/x.py')