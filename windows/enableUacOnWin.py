#!/bin/python

# enable User Access Control on Windows  

# run this script as admin

import colorama, os, sys, traceback 
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))

	if sys.platform == "win32": 
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
		os.system('ver')
		print(Style.RESET_ALL, end="")

		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))

		print("")

	else: 
		raise Exception("Sorry but this script only runs on Windows.")


def enableUac(): 
	print("\nEnable User Access Control on Windows.\n")

	try:
		checkOsForWindows()
		
		startDateTime = datetime.now()
		
		print("Started disabling User Access Control at", startDateTime.strftime("%m-%d-%Y %H:%M %p"))

		if os.system('reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f') != 0:
		
			raise Exception("Error occurred while enabling User Access Control")

		print(Fore.GREEN + "Successfully enabled User Access Control." + Style.RESET_ALL)

		finishedDateTime = datetime.now()

		print("Finished disabling User Access Control at", finishedDateTime.strftime("%m-%d-%Y %H:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

		print(Fore.BLUE + "Please save your documents and close your application.")
		input("Press any key to restart the computer:" + Style.RESET_ALL)
		
		if os.system('shutdown /r /t 0') != 0: 
			raise Exception("Error occurred while restarting computer.")

	except Exception: 
		print(Fore.RED + "Failed to enable User Access Control.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


enableUac()
