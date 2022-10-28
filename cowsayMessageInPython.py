#!/bin/python

# Cowsay message in Python
 
# you can run this script: python3 cowsayMessageInPython.py < message > 

import colorama, os, subprocess, sys, traceback
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
		
	elif sys.platfrom == "linux": 
		print(Fore.GREEN + "Operating System: ")
		os.system(uname -r)
		print(Style.RESET_ALL, end="")
		operatingSystem = "Linux"
		
	print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	print("")
	return operatingSystem
		

def checkCowsay(operatingSystem):
	print("Started checking Cowsay at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	FNULL = open(os.devnull, 'w')
	
	if operatingSystem == "Windows": 
	
		checkCowsayOnWindows = subprocess.call(['where', 'cowsay'], stdout=FNULL)
		
		if checkCowsayOnWindows == 0: 
			print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)
			
			print("Finished checking Cowsay at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
			print("")
			
		else: 
			print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)

			print("Finished checking Cowsay at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
			print("")
			
	elif operatingSystem == "macOS" or operatingSystem == "Linux": 
		
		checkCowsayOnMacOrLinux = subprocess.call(['which', 'cowsay'], stdout=FNULL)
		
		if checkCowsayOnMacOrLinux == 0: 
			print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)
			
			print("Finished checking Cowsay at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
			print("")
			
		else: 
			print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)
			
			print("Finished checking Cowsay at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
			print("")
			
	
def getCowMessage(operatingSystem): 
	if operatingSystem == "Windows": 
		cowMessage = str(input("Please type what you like the cow to say and press \"Enter\" key (Example: Moo!): \n"))
		
		print("")
		
	elif operatingSystem == "macOS" or operatingSystem == "Linux": 
		cowMessage = str(input("Please type what you like the cow to say and press \"return\" key (Example: Moo!): \n"))
		
		print("")
		
	return cowMessage
	
	
def checkParameters(cowMessage): 
	print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	valid = "true"
	
	print("Parameters: ")
	print("----------------------------------")
	print("cowMessage: {0}".format(cowMessage))
	print("----------------------------------")
	
	if cowMessage == None: 
		print(Fore.RED + "cowMessage is not set.")
		valid = "false"
		
	if valid == "true": 
		print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		exit("" + Style.RESET_ALL)
		

def cowsayMessage(): 
	print("\nCowsay message in Python.\n")
	
	operatingSystem = checkOs()
	checkCowsay(operatingSystem)

	if len(sys.argv) >= 2: 
		cowMessage = str(sys.argv[1])

	else: 
		cowMessage = getCowMessage(operatingSystem)
		
	checkParameters(cowMessage)

	try: 
		startDateTime = datetime.now()
		print("Cow started message at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

		cmd = "cowsay {0}".format(cowMessage)
		os.system(cmd)
		
		print(Fore.GREEN + "Cow successfully said message." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Cow finished message at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception as e: 
		print(Fore.RED + "Cow failed to say message.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)


cowsayMessage()
