#!/bin/python

# get square root in Python

# you can run this script with: python3 calculateSquareRootInPython.py < radicand >

import colorama, math, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs(): 
	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "win32": 
		print(Fore.GREEN + "Operating System: ", end=""); sys.stdout.flush()
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
	
	
def getRadicand(operatingSystem): 
	if operatingSystem == "Windows": 
		radicand = int(input("Please type the radicand and press the \"Enter\" key (Example: 36): "))
		
	else: 
		radicand = int(input("Please type the radicand and press the \"return\" key (Example: 36): "))
		
	print("")
	return radicand
	
	
def checkParameters(radicand):
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True 
	
	print("Parameter(s):")
	print("------------------------------")
	print("radicand: {0}".format(radicand))
	print("------------------------------")
	
	if radicand == None or radicand == "": 
		print(Fore.RED + "radicand is not set." + Style.RESET_ALL)
		valid = False 
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		raise Exception("One or more parameters are incorrect.")
		
		
def calculateSquareRoot(): 
	print("\nCalculate square root in Python.\n")
	operatingSystem = checkOs()

	if len(sys.argv) >= 2: 
		radicand = int(sys.argv[1])

	else: 
		radicand = getRadicand(operatingSystem)
	
	checkParameters(radicand)
	
	try: 
		startDateTime = datetime.now()
		print("Started calculating square root at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		squareRoot = math.sqrt(radicand) 
		print(Fore.BLUE + "The square root of {0} is {1}.".format(radicand, squareRoot))
		print(Fore.GREEN + "Successfully calculated  squareroot." + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished calculating square root at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception: 
		print(Fore.RED + "Failed to calculate square root.")
		traceback.print_exc()
		exit("")


calculateSquareRoot()
