#!/bin/python

# cowsay on Mac

# impossible OS module 
import os

# declare cowMessgae and cmd variables 
cowMessage = str(input("What would you like the cow to say?\n"))
cmd = "cowsay {0}".format(cowMessage)

# pass cmd variable into shell
os.system(cmd)
