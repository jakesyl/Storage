import os
'''
Cortex Storage
Replaces a files extension nwith ctx
'''
def fileReplace(path):
    os.remove(path)
    newPath = path + ".ctx"
    file = open(newpath, 'w+')
