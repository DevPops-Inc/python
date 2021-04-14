#!/bin/python

# create local admin on Windows

# import OS module 
import os

# prompt user input
str(input("Create local admin on Windows.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare localAdmin and localAdminPassword variables
localAdmin = str(input("What is the local admin username you wish to create? (Example: local.admin)\n"))
localAdminPassword = str(input("What the password you wish to create for this local admin? (Example: Password123)\n"))

# create local admin account 
createLocalAdmin = "net user /add {0} {1}".format(localAdmin, localAdminPassword)

# add local admin to administrators group
addLocalAdmintoAdminGroup = "net localgroup administrators {0} /add".format(localAdmin)

# set local admin password to never expire 
neverExpireLocalAdminPassword = "WMIC USERACCOUNT WHERE Name={0} SET PasswordExpires=FALSE".format(localAdmin)

# define localAdminCreation list and for loop
localAdminCreation = [createLocalAdmin, addLocalAdmintoAdminGroup, neverExpireLocalAdminPassword,'net user']

for create in localAdminCreation: 
    os.system(create)
