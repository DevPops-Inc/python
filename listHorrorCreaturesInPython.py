#!/bin/python

# add items to list examples

import colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "win32": 
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
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
		
	print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	print("")
	return operatingSystem


def listHorrorCreatures(): 
	print("\Let's list horror creatures in Python.\n")
	checkOs()
	
	try: 
		startDateTime = datetime.now()
		print("Started listing horror creatures at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
			
		horrorCreatures = ["Vampire", "Werewolf", "Witch", "Zombie"]

		for creature in horrorCreatures: 
			time.sleep(1)
			print(creature)

		time.sleep(2)
		print(Fore.YELLOW + "Wait!  There's something behind you!" + Style.RESET_ALL)
		
		horrorCreatures = horrorCreatures+["Ghost"]
		time.sleep(2)

		for creature in horrorCreatures: 
			time.sleep(1)
			print(creature)

		time.sleep(1)
		print(Fore.GREEN + "Successfully listed horror creatures." + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished listing horror creatures at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception as e: 
		print(Fore.RED + "Failed to list horror creatures.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)


listHorrorCreatures()
