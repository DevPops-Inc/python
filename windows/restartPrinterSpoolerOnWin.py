#!/bin/python

# restart printer spooler on Windows
# run this script as admin

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
		raise Exception("Sorry but this script only runs on Windows.")
		
		
def restartPrinterSpooler(): 
	print("\nRestart printer spooler on Windows.\n")
	
	try: 
		checkOsForWindows()
		
		startDateTime = datetime.now()

		print("Started restarting printer spooler at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

		printerSpooler = ['net stop spooler', 'net start spooler']

		for printer in printerSpooler:
			if os.system(printer) != 0: 
				raise Exception("Error occurred while restarting printer spooler.")
			
		print(Fore.GREEN + "Successfully restarted printer spooler." + Style.RESET_ALL)
	
		finishedDateTime = datetime.now()
		
		print("Finished restarting printer spooler at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime 
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception: 
		print(Fore.RED + "Failed to restart printer spooler.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)
		
		
restartPrinterSpooler()
