#!/bin/python

# create standard user on Windows

# run this script as admin
# you can run this script with: python3 createStandardUserOnWindows.py < standard user > < password > 

import colorama, getpass, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "win32": 
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
		os.system('ver')
		print(Style.RESET_ALL, end="")
		
		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		print("")
		
	else: 
		print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)
		
		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		
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
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True
	
	print("Parameter(s):")
	print("----------------------------------------------")
	print("standardUser        : {0}".format(standardUser))
	print("standardUserPassword: {0}".format("***"))
	print("----------------------------------------------")
	
	if standardUser == None: 
		print(Fore.RED + "standardUser is not set." + Style.RESET_ALL)
		valid = False
		
	if standardUserPassword == None: 
		print(Fore.RED + "standardUserPassword is not set." + Style.RESET_ALL)
		valid = False
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
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

		print("Started creating {0} at {1}".format(standardUser,startDateTime.strftime("%m-%d-%Y %I:%M %p")))
		
		createstandardUser = "net user /add {0} {1}".format(standardUser, standardUserPassword)

		neverExpireStandardUserPassword = "WMIC USERACCOUNT WHERE Name='{0}' SET PasswordExpires=FALSE".format(standardUser)

		standardUserCreation = [createstandardUser, neverExpireStandardUserPassword, 'net user']

		for create in standardUserCreation: 
			if os.system(create) != 0: 
				raise Exception("Attempt threw an error!")
			
		print(Fore.GREEN + "Successfully created {0}".format(standardUser)+ Style.RESET_ALL)
		
		finishedDateTime = datetime.now()

		print("Finished creating {0} at {1}".format(standardUser, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception: 
		print(Fore.RED + "Failed to create {0}".format(standardUser))
		
		traceback.print_exc()
		exit("" + Style.RESET_ALL)
		
		
createStandardUser()
