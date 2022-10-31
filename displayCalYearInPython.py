#!/bin/python

# display calendar year in Python

# you can run this script with: python3 displayCalYearInPython.py < calendar year >

import calendar, colorama, os, sys, traceback
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
		
	print("Finished checking operaring system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	print("")
	return operatingSystem
	
	
def getCalendarYear(operatingSystem): 
	if operatingSystem == "Windows": 
		calendarYear = int(input("Please type the year calendar year you wish to display and press the \"Enter\" key (Example: 1999): "))
		
		print("")
	
	elif operatingSystem == "macOS" or operatingSystem == "Linux": 
		calendarYear = int(input("Please type the year calendar year you wish to display and press the \"return\" key (Example: 1999): "))
		
		print("")
		
	return calendarYear
	
	
def checkParameters(calendarYear): 
	print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
	valid = "true"
	
	print("Parameters: ")
	print("--------------------------------------")
	print("calendarYear: {0}".format(calendarYear))
	print("--------------------------------------")
	
	if calendarYear == None: 
		print(Fore.RED + "calendarYear is not set." + Style.RESET_ALL)
		valid = "false"
		
	if valid == "true": 
		print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		print("")
		
	else: 
		print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
		
		print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
		exit("")
	

def displayYear(): 
	print("\nDisplay Calendar Year in Python.\n")
	operatingSystem = checkOs()
	
	if len(sys.argv) >= 2: 
		calendarYear = int(sys.argv[1])
		
	else: 
		calendarYear = getCalendarYear(operatingSystem)
		
	checkParameters(calendarYear)
	
	try: 
		startDateTime = datetime.now()
		print("Started displaying calendar year at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		print("")
		calendar.prcal(calendarYear)
		print("")
		
		print(Fore.GREEN + "Successfully displayed {0} calendar year.".format(calendarYear) + Style.RESET_ALL)
		
		finishedDateTime = datetime.now()
		print("Finished displaying calendar year at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))
		
		duration = finishedDateTime - startDateTime
		print("Total execution time: {0} second(s)".format(duration.seconds))
		print("")
		
	except Exception as e:
		print(Fore.RED + "Failed to display calendar year.")
		print(e)
		print(traceback.print_stack)
		exit("" + Style.RESET_ALL)
		
		
displayYear()
	