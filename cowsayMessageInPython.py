#!/bin/python

# Cowsay message in Python
 
# you can run this script: python3 cowsayMessageInPython.py "< message >"

import colorama, os, shlex, subprocess, sys, traceback
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
		
	elif sys.platfrom == "linux": 
		print(Fore.GREEN + "Operating System: ")
		os.system(uname -r)
		print(Style.RESET_ALL, end="")
		operatingSystem = "Linux"
		
	print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

	print("")
	return operatingSystem
		

def checkCowsay(operatingSystem):
	print("Started checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	FNULL = open(os.devnull,  'w')
	
	if operatingSystem == "Windows": 
		checkCowsayOnWindows = subprocess.call(['where', 'cowsay'], stdout=FNULL)
		
		if checkCowsayOnWindows == 0: 
			print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)
			
			print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
			print("")
			
		else: 
			raise Exception("Cowsay is not installed.")
			
	else: 
		checkCowsayOnMacOrLinux = subprocess.call(['which', 'cowsay'], stdout=FNULL)
		
		if checkCowsayOnMacOrLinux == 0: 
			print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)
			
			print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
			print("")
			
		else: 
			raise Exception("Cowsay is not installed.")
			
	
def getCowMessage(operatingSystem): 
	if operatingSystem == "Windows": 
		cowMessage = str(input("Please type what you like the cow to say and press \"Enter\" key (Example: Moo!): "))
		
	else: 
		cowMessage = str(input("Please type what you like the cow to say and press \"return\" key (Example: Moo!): "))
		
	print("")	
	return cowMessage
	
	
def checkParameters(cowMessage): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True
	
	print("Parameter(s): ")
	print("----------------------------------")
	print("cowMessage: {0}".format(cowMessage))
	print("----------------------------------")
	
	if cowMessage == None or cowMessage == "": 
		print(Fore.RED + "cowMessage is not set.")
		valid = False
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		raise Exception("One or more parameters are incorrect.")
		

def cowsayMessage(): 
	print("\nCowsay message in Python.\n")
	
	operatingSystem = checkOs()
	checkCowsay(operatingSystem)

	if len(sys.argv) >= 2: 
		cowMessage = str(sys.argv[1])

	else: 
		cowMessage = getCowMessage(operatingSystem)

	try: 
		checkParameters(cowMessage)

		startDateTime = datetime.now()
		print("Cow started message at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

		cmd = "cowsay {}".format(shlex.quote(cowMessage))
		os.system(cmd)
		print(Fore.GREEN + "Cow successfully said message." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Cow finished message at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Cow failed to say message.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


cowsayMessage()
