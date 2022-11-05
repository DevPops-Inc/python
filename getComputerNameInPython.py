#!/bin/python

# get computer name in Python

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
	print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	
	if sys.platform == "win32": 
		print(Fore.GREEN + "Operating System: ", end="")
		os.system('ver')
		print(Style.RESET_ALL, end="")
		operatingSystem = "Windows"
		
	elif sys.platform == "darwin": 
		print(Fore.GREEN + "Operating System: ")
		os.system('sw_vers')
		print(Style.RESET_ALL, end="")
		operatingSystem = "macOS"
		
	elif sys.platform == "linux":
		print(Fore.GREEN + "Operating System: ")
		os.system('uname -r')
		print(Style.RESET_ALL, end="")
		operatingSystem = "Linux"
		
	print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	print("")
	return operatingSystem
		
		
def getComputerName(): 
	print("\nGet computer name in Python.\n")
	checkOs()
	
	try: 
		startDateTime = datetime.now()
		print("Started getting computer name at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		print(Fore.BLUE + "The computer name is: ")
		os.system('hostname')
		print(Fore.GREEN + "Successfully got computer name." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Finished getting computer name at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception as e: 
		print(Fore.RED + "Failed to get computer name.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)


getComputerName()
