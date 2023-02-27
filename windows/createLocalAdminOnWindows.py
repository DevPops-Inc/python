#!/bin/python

# create local admin on Windows

# run this script as admin
# you can run this script with: python3 createLocalAdminOnWindows.py < local admin > < password > 

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

		
def getLocalAdmin(): 
	localAdmin = str(input("Please type the local admin username you wish to create and press the \"Enter\" key (Example: local.admin): "))

	print("")
	return localAdmin

def getLocalAdminPassword(): 
	localAdminPassword = getpass.getpass("Please the password you wish to create for this local admin and press the \"Enter\" key (Example: Password123): ")

	print("")
	return localAdminPassword


def checkParameters(localAdmin, localAdminPassword): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True

	print("Parameter(s):")
	print("------------------------------------------")
	print("localAdmin        : {0}".format(localAdmin))
	print("localAdminPassword: {0}".format("***"))
	print("------------------------------------------")

	if localAdmin == None: 
		print(Fore.RED + "localAdmin is not set." + Style.RESET_ALL)
		valid = False

	if localAdminPassword == None: 
		print(Fore.RED + "localAdminPassword is not set." + Style.RESET_ALL)
		valid = False

	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")

	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		exit("")


def createLocalAdmin(): 
	print("\nCreate local admin on Windows.\n")
	checkOsForWindows()

	if len(sys.argv) > 2: 
		localAdmin         = str(sys.argv[1])
		localAdminPassword = str(sys.argv[2])

	else: 
		localAdmin         = getLocalAdmin()
		localAdminPassword = getLocalAdminPassword()

	checkParameters(localAdmin, localAdminPassword)

	try: 
		startDateTime = datetime.now()
		print("Started creating local admin at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

		createLocalAdmin = "net user /add {0} {1}".format(localAdmin, localAdminPassword)
		addLocalAdmintoAdminGroup = "net localgroup administrators {0} /add".format(localAdmin)
		
		neverExpireLocalAdminPassword = "WMIC USERACCOUNT WHERE Name='{0}' SET PasswordExpires=FALSE".format(localAdmin)

		localAdminCreation = [createLocalAdmin, addLocalAdmintoAdminGroup, neverExpireLocalAdminPassword, 'net user']

		for create in localAdminCreation: 
			if os.system(create) != 0:
				raise Exception("Attempt threw an error!")

		print(Fore.GREEN + "Successfully created local admin." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Finished creating local admin at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Failed to create local admin.")
		
		traceback.print_exc()
		exit("" + Style.RESET_ALL)

createLocalAdmin()
