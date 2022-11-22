#!/bin/python

# launch YouTube in Chrome on Mac

# import OS module
import os

# prompt user input
str(input("\nLaunch YouTube in Chrome on Mac.\nPress any key to continue or press control and C keys to quit.\n"))

# launch YouTube in Chrome
youTubeInChrome=os.system('open -a "Google Chrome" http://youtube.com')
os.system(youTubeInChrome)
