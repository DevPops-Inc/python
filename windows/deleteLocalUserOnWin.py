#!/bin/python

# delete local user on Windows 

# you can run this script with: python3 deleteLocalUserOnWin.py < local user > 

import colorama, os, sys, traceback
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
		raise Exception("Sorry but this script only runs on Windows.")
		

def getLocalUser(): 
	os.system('net user')

	localUser = str(input("Please type the user to you wish to delete and press the \"Enter\" (Example: old.user) key: "))

	print("")
	return localUser


def checkParameters(localUser):
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True

	print("Parameter(s):")
	print("--------------------------------")
	print("localUser: {0}".format(localUser))
	print("--------------------------------")

	if localUser == None or localUser == "": 
		print(Fore.RED + "localUser is not set." + Style.RESET_ALL)
		valid = False

	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")

	else: 
		raise Exception("One or more parameters are incorrect.")


def deleteLocalUser(): 
	print("\nDelete local users on Windows.\n")
	checkOsForWindows()

	if len(sys.argv) >= 2: 
		localUser = str(sys.argv[1])

	else: 
		localUser = getLocalUser()

	checkParameters(localUser)

	try: 
		startDateTime = datetime.now()
		
		print("Started deleting {0} at {1}".format(localUser, startDateTime.strftime("%m-%d-%Y %I:%M %p")))

		deleteUser = "net user {0} /delete".format(localUser)

		if os.system(deleteUser) != 0: 
			raise Exception("Error occurred while deleting local user.")

		print("The remaining users are:" + Fore.BLUE)
		os.system('net user')
		print(Fore.GREEN + "Successfully deleted {0}".format(localUser) + Style.RESET_ALL)

		finishedDateTime = datetime.now()

		print("Finished deleting {0} at {1}".format(localUser, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Failed to delete {0}".format(localUser))
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


deleteLocalUser()
