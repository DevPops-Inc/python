#!/bin/python

# cowsay on Mac

# import OS module 
import os

# prompt user input 
str(input("Cowsay on Mac.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare cowMessgae and cmd variables 
cowMessage = str(input("What would you like the cow to say?\n"))
cmd = "cowsay {0}".format(cowMessage)

# pass cmd variable into shell
os.system(cmd)
