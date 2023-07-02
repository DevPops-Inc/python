#!/bin/python

# convert subnet to binary 

# you can run this script with: python3 convertSubnetToBinInPython.py < subnet >

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime 
colorama.init()


def checkOs(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "Win32": 
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
		os.system('ver')
		print(Style.RESET_ALL, end="")
		operatingSystem = "Windows"
		
	elif sys.platform == "darwin": 
		print(Fore.GREEN + "Operating System:")
		os.system('sw_vers')
		print(Style.RESET_ALL, end="")
		operatingSystem = "macOS"
		
	elif sys.platform == "linux": 
		print(Fore.GREEN + "Operating System:")
		os.system('uname -r')
		print(Style.RESET_ALL, end="")
		operatingSystem = "Linux"
		
	print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	print("")
	return operatingSystem
	
	
def getSubnet(operatingSystem):
	if operatingSystem == "Windows": 
		subnet = int(input("Please type the subnet you wish to convert to binary and press the \"Enter\" key (Example: 28): "))
		
	else: 
		subnet = int(input("Please type the subnet you wish to convert to binary and press the \"return\" key (Example: 28): "))
		
	print("")
	return subnet


def checkParameters(subnet): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True 
	
	print("Parameter(s):")
	print("--------------------------")
	print("subnet: {0}".format(subnet))
	print("--------------------------")
	
	if subnet == None or subnet == "": 
		print(Fore.RED + "subnet is not set." + Style.RESET_ALL)
		valid = False 
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		exit("")
			
			
def convertSubnetToBinary(): 
	print("\nConvert subnet to binary in Python.\n")
	operatingSystem = checkOs()
	
	if len(sys.argv) >= 2: 
		subnet = int(sys.argv[1])
		
	else: 
		subnet = getSubnet(operatingSystem)
	
	checkParameters(subnet)
	
	try: 
		startDateTime = datetime.now()
		
		print("Started converting subnet to binary at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		subnetInBinary = format(subnet, 'b')
		print(Fore.BLUE + "The {0} subnet in binary is: {1}".format(subnet, subnetInBinary))
		print(Fore.GREEN + "Successfully converted subnet to binary." + Style.RESET_ALL)

		finishedDateTime = datetime.now()

		print("Finished converting subnet to binary at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Failed to convert subnet to binary.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


convertSubnetToBinary()
