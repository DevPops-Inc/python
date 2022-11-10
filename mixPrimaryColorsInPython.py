#!/bin/python

# mix primary colors in Python

# you can run this script with: python3 mixPrimaryColorsInPython.py < first color > < second color >

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System: ", end="")
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
    
    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def getColor1(operatingSystem):
	print("The primary colors are: ")

	print(Fore.RED + "red" + Style.RESET_ALL + ", "  + Fore.BLUE + "blue" + Style.RESET_ALL + ", and " + Fore.YELLOW + "yellow." + Style.RESET_ALL)

	print("")

	if operatingSystem == "Windows": 
		color1 = str(input("Please type the first color you want and press \"Enter\" key (Example: red): "))
		
		print("")
	
	elif operatingSystem == "macOS" or operatingSystem == "Linux":
		color1 = str(input("Please type the first color you want and press \"return\" key (Example: red): "))
		
		print("")
		
	return color1
		
	
def getColor2(operatingSystem): 
	if operatingSystem == "Windows": 
		color2 = str(input("Please type the second color you want and press \"Enter\" key (Example: blue): "))
		
		print("")
	
	elif operatingSystem == "macOS" or operatingSystem == "Linux": 
		color2 = str(input("Please type the second color you want and press \"return\" key (Example: blue): "))
		
		print("")
		
	return color2

	
def checkParameters(color1, color2): 
	print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	valid = "true"
	
	print("Parameters: ")
	print("--------------------------")
	print("color1: {0}".format(color1))
	print("color2: {0}".format(color2))
	print("--------------------------")
	
	if color1 == None: 
		print(Fore.RED + "color1 is not set." + Style.RESET_ALL)
		valid = "false"
		
	if color2 == None: 
		print(Fore.RED + "color2 is not set." + Style.RESET_All)
		valid = "false"
		
	if valid == "true":
		print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		exit("")
	

def mixPrimaryColors(): 
	print("\nLet's mix primary colors in Python.\n")
	operatingSystem =	checkOs() 
	
	if len(sys.argv) > 2: 
		color1 = str(sys.argv[1])
		color2 = str(sys.argv[2])

	else: 
		color1 = getColor1(operatingSystem)
		color2 = getColor2(operatingSystem) 
	
	checkParameters(color1, color2)
	
	try: 
		startDateTime = datetime.now()
		print("Started mixing colors at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		purple = '\033[35m'
		orange = '\033[33m'

		if (color1 == "red" or color1 == "blue") and (color2 == "blue" or color2 == "red"):
			print(purple + "You just made purple!" + Style.RESET_ALL) 
			print("")

		if (color1 == "red" or color1 == "yellow") and (color2 == "yellow" or color2 == "red"):
			print(orange + "You just made orange!" + Style.RESET_ALL) 
			print("")

		if (color1 == "blue" or color1 == "yellow") and (color2 == "yellow" or color2 == "blue"):
			print(Fore.GREEN + "You just made green!" + Style.RESET_ALL)
			print("")

		if color1 == color2:
			print(Fore.RED + "Error: you didn't mix a new color!" + Style.RESET_ALL)
			print("")
		
		finishedDateTime = datetime.now()
		print("Finished mixing colors at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
	
	except Exception as e: 
		print(Fore.RED + "Failed to mix colors.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)
		

mixPrimaryColors()
