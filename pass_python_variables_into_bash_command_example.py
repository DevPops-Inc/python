#!/bin/python

# pass Python variables into Bash command example

# import OS module 
import os

# declare cowMessgaes and cmd variables 
cowMessage1 = str(input("What would you like the cow to say?\n"))
cowMessage2 = str(input("Now what would you like the cow to say?\n"))
cmd = "cowsay {0} {1}".format(cowMessage1, cowMessage2)

# pass cmd variable into shell
os.system(cmd)
