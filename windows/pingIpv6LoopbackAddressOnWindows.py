#!/bin/python

# ping loopback IPv6 address on Windows

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
			
			
def pingLoopbackIpv6Address(): 
	print("\nPing loopback IPv6 address on Windows.\n")
	checkOsForWindows()
	
	try: 
		startDateTime = datetime.now()
		print("Started pinging loopback IPv6 address at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		if os.system('ping ::1') != 0: 
			raise Exception("Attempt threw an error!")
			
		print(Fore.GREEN + "Successfully pinged loopback IPv6 address." + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished pining loopback IPv6 address at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception: 
		print(Fore.RED + "Failed to ping loopback IPv6 address.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)
		
		
pingLoopbackIpv6Address()
