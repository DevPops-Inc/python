#!/bin/python

# Windows maintenance

# import OS module 
import os 

# prompt user input 
str(input("Windows maintenance.\nPress any key to continue.\n"))

# define maintenance list and for loop 
maintenance = ['echo y | chkdsk /f/r c:', 'SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth', 'defrag c: /u']

for job in maintenance: 
    os.system(job)

# prompt user save documents before restart
str(input("Please save your work and close applications.\nPress any key to continue.\n"))
os.system('shutdown /r /t 0')
