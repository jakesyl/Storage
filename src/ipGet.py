bashCommand = "ipconfig getifaddr en1"
import subprocess as sp
process = sp.Popen(bashCommand.split(), stdout=sp.PIPE)
output = process.communicate()[0]
print output
