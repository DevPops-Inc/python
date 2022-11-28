#!/bin/python

# create standard user on Windows

# run this script as admin
# you can run this script with: python3 createStandardUserOnWindows.py < standard user > < password > 

import colorama, getpass, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
	print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	
	if sys.platform == "win32": 
		print("Operating System: ", end="")
		os.system('ver')
		print(Style.RESET_ALL, end="")
		
		print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)
		
		print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		exit("")
		

def getStandardUser(): 
	standardUser = str(input("Please type the username you wish to create and press the \"Enter\" key (Example: standard.user): "))

	print("")
	return standardUser
	
	
def getStandardUserPassword(): 
	standardUserPassword = getpass.getpass("Please type the password you wish to create for this user and press the \"Enter\" key (Example: Password123): ")

	print("")
	return standardUserPassword


def checkParameters(standardUser, standardUserPassword): 
	print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	valid = "true"
	
	print("Parameters")
	print("----------------------------------------------")
	print("standardUser        : {0}".format(standardUser))
	print("standardUserPassword: {0}".format("***"))
	print("----------------------------------------------")
	
	if standardUser == None: 
		print(Fore.RED + "standardUser is not set." + Style.RESET_ALL)
		valid = "false"
		
	if standardUserPassword == None: 
		print(Fore.RED + "standardUserPassword is not set." + Style.RESET_ALL)
		valid = "false"
		
	if valid == "true": 
		print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		exit("")
		
		
def createStandardUser(): 
	print("\nCreate standard user on Windows.\n")
	checkOsForWindows()
	
	if len(sys.argv) > 2: 
		standardUser         = str(sys.argv[1])
		standardUserPassword = str(sys.argv[2])
		
	else: 
		standardUser         = str(getStandardUser())
		standardUserPassword = str(getStandardUserPassword())
		
	checkParameters(standardUser, standardUserPassword)
	
	try: 
		startDateTime = datetime.now()
		print("Started creating standard user at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		createstandardUser = "net user /add {0} {1}".format(standardUser, standardUserPassword)

		neverExpireStandardUserPassword = "WMIC USERACCOUNT WHERE Name= {0} SET PasswordExpires=FALSE".format(standardUser)

		standardUserCreation = [createstandardUser, neverExpireStandardUserPassword, 'net user']

		for create in standardUserCreation: 
			os.system(create)
			
		print(Fore.GREEN + "Successfully created standard user: {0}".format(standardUser)+ Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception as e: 
		print(Fore.Red)
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)
		
		
createStandardUser()