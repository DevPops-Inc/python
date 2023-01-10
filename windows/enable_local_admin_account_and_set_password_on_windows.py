#!/bin/python

# enable local admin account and set password on Windows

# you can run this script with: python3 enableLocalAdminAndSetPwOnWindows.py < local admin password > 

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
		
		
def getLocalAdminPw(): 
	localAdminPw = getpass.getpass("Please type the password for the local admin account and press the \"Enter\" key (Example: Password123): ")
	
	print("")
	return localAdminPw


def checkParameters(localAdminPw): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = "true"
	
	print("Parameter(s):")
	print("-------------------------------")
	print("localAdminPw: {0}",format("***"))
	print("-------------------------------")
	
	if localAdminPw == None: 
		print(Fore.RED + "localAdminPw is not set." + Style.RESET_ALL)
		valid = "false"
		
	if valid == "true": 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		exit("")
		

def enableLocalAdminAndSetPw(): 
	print("\nEnable local admin and set passsword on Windows.\n")
	checkOsForWindows()

	if len(sys.argv) >= 2: 
		localAdminPw = str(sys.argv[1])

	else: 
		localAdminPw = getLocalAdminPw()

	checkParameters(localAdminPw)
	
	try:
		startDateTime = datetime.now()
		print("Started enabling local admin and setting password at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		setLocalAdminPassword = "net user administrator {0}".format(localAdminPw)

		enableLocalAdmin = ['net user administrator /active:yes', setLocalAdminPassword, "WMIC USERACCOUNT WHERE Name='administrator' SET PasswordExpires=FALSE", 'net user administrator | findstr /C:expires']
	
		for enable in enableLocalAdmin:
			if os.system(enable) != 0: 
				raise Exception("Attempt threw an error!")
				
		finishedDateTime = datetime.now()
		print("Finished enabling local admin and setting password at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception as e: 
		print(Fore.RED + "Failed to enable local admin and set password.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)
		
		
enableLocalAdminAndSetPw()
