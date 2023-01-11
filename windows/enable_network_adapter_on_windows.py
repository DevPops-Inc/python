#!/bin/python 

# enable network adapter on Windows

# you can run this script with: python3 enableNetworkAdapaterOnWindows.py < network adapter >

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
		print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)
		
		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		exit("")
		

def getNetworkAdapter(): 
	os.system('netsh interface show interface')

	networkAdapter = str(input("Please type the interface name of the network adapter you wish to enable and press the \"Enter\" key (Example: Wi-Fi): "))
	
	print("")
	return networkAdapter


def checkParameters(networkAdapter): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

	valid = "true"
	
	print("Parameter(s):")
	print("------------------------------------------")
	print("networkAdapter: {0}".format(networkAdapter))
	print("------------------------------------------")
	
	if networkAdapter == None: 
		print(Fore.RED + "networkAdapter is not set." + Style.RESET_ALL)
		valid = "false"
		
	if valid == "true": 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		exit("")
		

def enableNetworkAdapter(): 
	print("\nEnable network adapter on Windows.\n")
	checkOsForWindows()
	
	if len(sys.argv) >= 2:
		networkAdapter = str(sys.argv[1])

	else: 
		networkAdapter = getNetworkAdapter()

	checkParameters(networkAdapter)

	try: 
		startDateTime = datetime.now()
		
		print("Started enabling {0} at {1}".format(networkAdapter, startDateTime.strftime("%m-%d-%Y %I:%M: %p")))

		enableNetworkAdapter = "netsh interface set interface {0} enable".format(networkAdapter)
		
		if os.system(enableNetworkAdapter) != 0: 
			raise Exception("Attempt threw an error!")

		os.system('netsh interface show interface')
		
		print(Fore.GREEN + "Successfully enabled {0}.".format(networkAdapter) + Style.RESET_ALL)		

		finishedDateTime = datetime.now()
		print("Finished enabling {0} at {1}".format(networkAdapter, finishedDateTime))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception as e: 
		print(Fore.RED + "Failed to enable {0}.".format(networkAdapter))
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)


enableNetworkAdapter()
