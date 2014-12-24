#!/usr/bin/python
from ipGet import ipget
from counting import counting
import Dbsetup

ip = ipget()# for local network storage
remove_dirs = counting()
count = remove_dirs[0]#remove_dirs is split up into directories to remove and number of directories
remove_dirs.remove[0]#not sure if thats a thing
Dbsetup.makedb()
