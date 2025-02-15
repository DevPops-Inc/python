#!/bin/python

# mix primary colors in Python

# you can run this script with: python3 mixPrimaryColorsInPython.py < first color > < second color >

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"
    
    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def getColor1(operatingSystem):
	print("The primary colors are: ")

	print(Fore.RED + "red" + Style.RESET_ALL + ", "  + Fore.BLUE + "blue" + Style.RESET_ALL + ", and " + Fore.YELLOW + "yellow." + Style.RESET_ALL)

	print("")

	if operatingSystem == "Windows": 
		color1 = str(input("Please type the first color you want and press \"Enter\" key (Example: red): "))
	
	elif operatingSystem == "macOS" or operatingSystem == "Linux":
		color1 = str(input("Please type the first color you want and press \"return\" key (Example: red): "))
		
	print("")	
	return color1
		
	
def getColor2(operatingSystem): 
	if operatingSystem == "Windows": 
		color2 = str(input("Please type the second color you want and press \"Enter\" key (Example: blue): "))
	
	elif operatingSystem == "macOS" or operatingSystem == "Linux": 
		color2 = str(input("Please type the second color you want and press \"return\" key (Example: blue): "))
		
	print("")	
	return color2

	
def checkParameters(color1, color2): 
	print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
	valid = True
	
	print("Parameter(s): ")
	print("--------------------------")
	print("color1: {0}".format(color1))
	print("color2: {0}".format(color2))
	print("--------------------------")
	
	if color1 == None or color1 == "": 
		print(Fore.RED + "color1 is not set." + Style.RESET_ALL)
		valid = False
		
	if color2 == None or color2 == "": 
		print(Fore.RED + "color2 is not set." + Style.RESET_All)
		valid = False
		
	if valid == True:
		print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)
		
		print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
		print("")
		
	else: 
		raise Exception("One or more parameter checks are incorrect.")
	

def mixPrimaryColors(): 
	print("\nLet's mix primary colors in Python.\n")
	operatingSystem =	checkOs() 
	
	if len(sys.argv) > 2: 
		color1 = str(sys.argv[1])
		color2 = str(sys.argv[2])

	else: 
		color1 = getColor1(operatingSystem)
		color2 = getColor2(operatingSystem) 
	
	try:
		checkParameters(color1, color2)

		startDateTime = datetime.now()
		print("Started mixing colors at", startDateTime.strftime("%m-%d-%Y %I:%M %p")) 

		if color1 == color2:
			raise Exception("You didn't mix a new color!")
		
		purple = '\033[35m'
		orange = '\033[33m'

		if (color1 == "red" or color1 == "blue") and (color2 == "blue" or color2 == "red"):
			print(purple + "You just made purple!" + Style.RESET_ALL) 

		if (color1 == "red" or color1 == "yellow") and (color2 == "yellow" or color2 == "red"):
			print(orange + "You just made orange!" + Style.RESET_ALL) 

		if (color1 == "blue" or color1 == "yellow") and (color2 == "yellow" or color2 == "blue"):
			print(Fore.GREEN + "You just made green!" + Style.RESET_ALL)

		primaryColors = [ "red", "blue", "yellow" ]

		if color1 not in primaryColors or color2 not in primaryColors:
			raise Exception("You didn't choose a primary color!")
				
		print(Fore.GREEN + "Successfully mixed colors." + Style.RESET_ALL)

		finishedDateTime = datetime.now()
		print("Finished mixing colors at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
	
	except Exception: 
		print(Fore.RED + "Failed to mix colors.")
		traceback.print_exc()
		exit("" + Style.RESET_ALL)
		

mixPrimaryColors()
