#!/bin/python

# pass Python variables into Bash command example

# import OS module 
import os

# prompt user input
str(input("\nPass Python varibles into Bash command example.\nPress any key to continue or press control and C keys to quit.\n"))

# declare cowMessgaes and cmd variables 
cowMessage1 = str(input("\nWhat would you like the cow to say?\n"))
cowMessage2 = str(input("\nNow what would you like the cow to say?\n"))
cmd = "\ncowsay {0} {1}".format(cowMessage1, cowMessage2)

# pass cmd variable into shell
os.system(cmd)
