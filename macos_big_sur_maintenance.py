#!/bin/python 

# macOS Big Sur maintenance 

# import OS module
import os

# prompt user input
str(input("macOS Big Sur maintenance.\nPress any key to continue or press control and C keys to quit.\n"))

# define maintenance list 
maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all', 'diskutil verifyVolume "MacOS"', 'diskutil repairVolume "MacOS"']

# define maintenance for loop
for jobs in maintenance: 
    os.system(jobs)

# prompt user for input and restart Mac
str(input("Please save your documents and close applications.\nPress any key to restart Mac."))
os.system('shutdown -r now')
