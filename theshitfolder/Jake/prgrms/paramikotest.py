import Crypto
import paramiko
import interactive

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect(
stdin, stdout, stderr = client.exec_commands('insert commands here')
#so what i'm going to end up doing is cd into the users directory (as in the user who's stuff we are updating, and then upload the stuff there however the fuck that's done
for line in stdout:
    #do something
client.close()
