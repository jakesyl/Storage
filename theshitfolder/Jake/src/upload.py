#import ecdsa#don't know if this is neccesary
#import Crypto
import paramiko
import logging
#import interactive #cances are this doesn't actually exsist
def upload():
	logger = logging.getLogger(__name__)
	try:
	    client = paramiko.SSHClient()
	    client.load_system_host_keys()
	    client.set_missing_host_key_policy(paramiko.WarningPolicy)

	    client.connect('2601:c:3480:379:aa20:66ff:fe35:3e73', 22, 'jcortex', 'jake1998')#username may be wrong

	    #so what i'm going to end up doing is cd into the users directory (as in the user who's stuff we are updating, and then upload the stuff there however the fuck that's done
	    stdin, stdout, stderr = client.exec_command('ls')
	    print stdout.read(),
	except Exception, e: # will catch later
		print str(e)
	finally:
	    client.close()


#after this works you need to find a way to get name and pass on their computer
upload()