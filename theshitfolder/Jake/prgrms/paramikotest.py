#import ecdsa#don't know if this is neccesary
#import Crypto
import paramiko
#import interactive #cances are this doesn't actually exsist

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect('localhost', 22, 'Jakes-MacBook-Pro-3', 'jake1998')#username may be wrong
stdin, stdout, stderr = client.exec_commands('ls')
#so what i'm going to end up doing is cd into the users directory (as in the user who's stuff we are updating, and then upload the stuff there however the fuck that's done
for line in stdout:
    #do something
    print line
client.close()
#after this works you need to find a way to get name and pass on their computer
