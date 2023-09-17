#!/bin/python 

# disable network adapter on Windows 

# you can run this script with: python3 disableNetworkAdapterOnWindows.py < network adapter >

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

	networkAdapter = str(input("Please type the interface name of the network adapter you wish to disable and press the \"Enter\" key (Example: Wi-Fi): "))
	
	print("")
	return networkAdapter


def checkParameters(networkAdapter): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True
	
	print("Parameter(s):")
	print("------------------------------------------")
	print("networkAdapter: {0}".format(networkAdapter))
	print("------------------------------------------")
	
	if networkAdapter == None or networkAdapter == "": 
		print(Fore.RED + "networkAdapter is not set." + Style.RESET_ALL)
		valid = False
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p")) 
		exit("")
		

def disableNetworkAdapter(): 
	print("\nDisable network adapter on Windows.\n")
	checkOsForWindows()
	
	if len(sys.argv) >= 2:
		networkAdapter = str(sys.argv[1])

	else: 
		networkAdapter = getNetworkAdapter()

	checkParameters(networkAdapter)

	try: 
		startDateTime = datetime.now()
		
		print("Started disabling {0} at {1}".format(networkAdapter, startDateTime.strftime("%m-%d-%Y %I:%M: %p")))

		disableNetworkAdapter = "netsh interface set interface {0} disable".format(networkAdapter)
		
		if os.system(disableNetworkAdapter) != 0: 
			raise Exception("Error occurred while disabling network adapter.")

		os.system('netsh interface show interface')
		
		print(Fore.GREEN + "Successfully disabled {0}.".format(networkAdapter) + Style.RESET_ALL)		

		finishedDateTime = datetime.now()
		print("Finished disabling {0} at {1}".format(networkAdapter, finishedDateTime))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Failed to disable {0}.".format(networkAdapter))
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


disableNetworkAdapter()
