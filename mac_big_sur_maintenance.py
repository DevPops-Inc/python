#!/bin/python 

# Mac Big Sur maintenance 

# import OS module
import os

# define maintenance list 
maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all', 'diskutil verifyVolume "MacOS"', 'diskutil repairVolume "MacOS"']

# define maintenance for loop
for jobs in maintenance: 
    os.system(jobs)

# prompt user for input 
print("Save your documents and close applications.")
input("Press any key to restart Mac.")

# restart mac
os.system(shutdown -r now)
