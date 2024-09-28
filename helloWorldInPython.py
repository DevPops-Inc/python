#!/bin/python

# hello world exercise in Python

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
		
	elif sys.platform == "darwin": 
		print(Fore.GREEN + "Operating System:")
		os.system('sw_vers')
		print(Style.RESET_ALL, end="")
		
	elif sys.platform == "linux": 
		print(Fore.GREEN + "Operating System:")
		os.system('uname -r')
		print(Style.RESET_ALL, end="")
			
	print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	print("")
	

def helloWorldExercise():
	print("\nHello world exercise in Python.\n")
	checkOs()
	
	try: 
		startDateTime = datetime.now()
		print("Started hello world exercise at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		colors = dict(Fore.__dict__.items())

		for color in colors.keys():
			time.sleep(.25)
			print(colors[color] + "Hello, World!")
			
		print(Fore.GREEN + "Successfully executed hello world exercise." + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished hello world exercise at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")

	except Exception: 
		print(Fore.RED + "Failed to perform hello world exercise.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)

		
helloWorldExercise()
