#!/bin/python

# disable admin password expiration on Windows 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "win32": # Windows logging looks weird in Python 3.11
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
		os.system('ver')
		print(Style.RESET_ALL, end="")
		
		print("Finished checking operating system", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)
		
		print("Finished checking operating system", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		exit("")
		
		
def disableAdminPwExpir(): 
	print("\nDisable admin password expiration on Windows.\n")
	checkOsForWindows()
	
	try: 
		startDateTime = datetime.now()
		print("Started disabling admin password expiration at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		if os.system("WMIC USERACCOUNT WHERE Name='Administrator' SET PasswordExpires=FALSE") != 0:
			raise Exception("Attempt threw an error!")

		os.system('net user Administrator')
		print(Fore.GREEN + "Successfully disabled admin password expiration." + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished disabling admin password expiration at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime 
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception as e:
		print(Fore.RED + "Failed to disable admin password expiration.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)
		
		
disableAdminPwExpir()
