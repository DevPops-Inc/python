#!/bin/python

# clear Python Screen on Mac

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

    print("Finished checking operating system at", datetime.now())

    print("")
    return operatingSystem


def clearScreen():
    print("\nClear screen in Python.\n")
    operatingSystem = checkOs()

    try: 
        startDateTime = datetime.now()
        
        print("Started clearing screen at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if operatingSystem == "Windows": 
            os.system('cls')
            
        else: 
            os.system('clear')

        finishedDateTime = datetime.now()

        print("Finished clearing screen at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime

        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to clear screen.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


clearScreen()
