#!/bin/python

# write pi to a file in Python

# you can run this script with: python3 writePiToFileInPython.py "< filename >""

import colorama, math, os, pathlib, sys, traceback
from colorama import Fore, Style 
from datetime import datetime 
from pathlib import Path
colorama.init()


def checkOs(): 

	print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	
	if sys.platform == "win32": 
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
	
	
def getFilename(operatingSystem): 
	if operatingSystem == "Windows": 

		filename = str(input("Please type the filename and press the \"Enter\" key (Example: pi.txt): "))
		
	else: 

		filename = str(input("Please type the filename and press the \"return\" key (Example: pi.txt): "))
		
	print("")
	filename = Path(filename)
	return filename 
		

def checkParameters(filename): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True 
	
	print("Parameter(s):")
	print("------------------------------")
	print("filename: {0}".format(filename))
	print("------------------------------")
	
	if filename == None or filename == "": 
		print(Fore.RED + "filename is not set." + Style.RESET_ALL)
		valid = False 
		
	if valid == True: 
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

		print("")
		
	else: 
		raise Exception("One or more parameters are incorrect.")


def checkIfFileExists(operatingSystem, filename): 

	print(Fore.BLUE + "Do you want to overwrite the {0} file?".format(filename) + Style.RESET_ALL)

	if operatingSystem == "Windows":
		choice = input("Please type \"Y\" or \"N\" and press the \"Enter\" key: ")

	else: 
		choice = input("Please type \"Y\" or \"N\" and press the \"return\" key: ")

	print("")
	return choice


def deletePiFile(operatingSystem, filename): 
	print(Fore.BLUE + "Do you want to delete the {0} file?".format(filename)+ Style.RESET_ALL)

	if operatingSystem == "Windows": 
		choice = input("Please type \"Y\" or \"N\" and press the \"Enter\" key: ")

	else: 
		choice = input("Please type \"Y\" or \"N\" and press the \"return\" key: ")

	print("")
	return choice


def writePiToFile(): 
	print("\nLet's write the value of Pi to a file in Python.\n")

	try: 
		operatingSystem = checkOs()
	
		if len(sys.argv) >= 2: 
			filename = str(sys.argv[1])
			
		else: 
			filename = getFilename(operatingSystem)

		checkParameters(filename)

		if	os.path.exists(filename) == True: 
			choice = checkIfFileExists(operatingSystem, filename)

			if choice == "N" or choice == "n": 
				exit("Please run this script again and type a different filename next time around.")

		startDateTime = datetime.now()

		print("Started writing the value of Pi to file at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		pi=math.pi
		t=open(filename, "w")
		t.write("The value of Pi is: {0}".format(pi))
		t.close()

		r=open(filename)
		print(Fore.BLUE + r.read())
		print(Fore.GREEN + "Successfully wrote the value of Pi to a file." + Style.RESET_ALL)
		r.close()
		print("")

		choice = deletePiFile(operatingSystem, filename)
		
		if choice == "Y" or choice == "y": 
			os.remove(filename)

		finishedDateTime = datetime.now()
		
		print("Finished writing the value of Pi to file at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception: 
		print(Fore.RED + "Failed to write value of Pi to a file.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)
		
		
writePiToFile()
