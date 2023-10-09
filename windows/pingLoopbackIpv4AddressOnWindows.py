#!/bin/python

# ping loopback IPv4 address on Windows

# haven't this script tested on Winodws yet 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime 
colorama.init()


def checkOsForWindows(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "Win32": 
		print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
		os.system('ver')
		print(Style.RESET_ALL, end="")

		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		print("")

	else: 
		print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		exit("")


def pingLoopbackIpv4Address(): 
	print("\nPing loopback IPv4 address on Windows.")
	checkOsForWindows()

	try: 
		startDateTime = datetime.now()
		print("Started pinging loopback IPv4 address at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

		if os.system('ping 127.0.0.1') != 0: 
			raise Exception("Error occurred while pinging loopback IPv4 address.")
		
		print(Fore.GREEN + "Successfully pinged loopback IPv4 address." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Finished pinging loopback IPv4 address at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception:
		print(Fore.RED + "Failed to ping loopback IPv4 address.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)


pingLoopbackIpv4Address()
