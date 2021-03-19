#!/bin/python

# Windows maintenance

# import OS module 
import os 

# define maintenance list
maintenance = ['echo y | chkdsk /f/r c:', 'SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth', 'defrag c: /u']

# define maintenance for loop
for job in maintenance: 
    os.system(job)

# print message to user and wait for user input
str(input("Please save your work and close applications. Press any key to restart Windows"))

# restart Windows
os.system('shutdown /r /t 0')
    