import os
#Stops crawling .dotfiles
root = os.path.expanduser('~')
for dir_name, sub_dirs, files in os.walk(root):
	print files
	for afile in files:
		if (dot(afile)==True):
			continue

def dot(afile):
	if (afile[1] == '.'):
		return True
	else:
		return False