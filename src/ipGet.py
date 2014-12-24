#!/usr/bin/python
import subprocess


def ipget():
    bashCommand = "ipconfig getifaddr en1"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output
