#!/bin/python

# Windows maintenance

# import OS module 
import os 

# define maintenance and restart lists
maintenance = ['echo y | chkdsk /f/r c:', 'SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth', 'defrag c: /u']
restart = ['pause', 'shutdown /r /t 0']

# define maintenance for loop
for job in maintenance: 
    os.system(job)

# print message to user
print("Please save your work and close applications.")

# define restart for loop
for job in restart: 
    os.system(job)
    