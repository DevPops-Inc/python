#!/bin/python

# display home directory

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from pathlib import Path
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


def displayHomeDir(): 
    print("\nDisplay directory directory.\n")
    operatingSystem = checkOs()

    try: 
        startDateTime = datetime.now()
        print("Started displaying home directory at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        homeDir=Path.home()
        print(Fore.BLUE + "Your home directory is: {0}".format(homeDir))
        print(Fore.GREEN + "Successfully displayed home directory." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished displaying home directory at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
    
    except Exception as e: 
        print(Fore.RED + "Failed to display home directory.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


displayHomeDir()
