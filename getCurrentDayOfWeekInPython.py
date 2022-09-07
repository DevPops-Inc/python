#!/bin/python

# get current day of week

import colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        os.system('ver')
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")
    return operatingSystem


def getCurrentDayOfWeek(): 
    print("\nGet current day of the week in Python.\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        
        print("Started getting current day of the week at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print(Fore.BLUE + "The current day of the week is: {0}.".format(time.strftime('%A')))
        print(Fore.GREEN + "Successfully got the current day of the week." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting current day of the week at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to get current day of the week.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getCurrentDayOfWeek()
