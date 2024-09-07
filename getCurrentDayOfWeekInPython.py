#!/bin/python

# get current day of week in Python

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
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")


def getCurrentDayOfWeek(): 
    print("\nGet current day of the week in Python.\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        
        print("Started getting current day of the week at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
        
        print(Fore.BLUE + "The current day of the week is: {0}.".format(time.strftime('%A')))
        print(Fore.GREEN + "Successfully got the current day of the week." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting current day of the week at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to get current day of the week.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getCurrentDayOfWeek()
