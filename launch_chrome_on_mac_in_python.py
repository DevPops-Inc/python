#!/bin/python

# launch Chrome on Mac

# import OS module
import os

# prompt user input
str(input("Launch Chrome on Mac.\nPress any key to continue or press control and C keys to quit.\n"))

# launch Chrome
browser=os.system('open -a "Google Chrome"')
