#!/bin/python

# get local users on Windows 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        raise Exception("Sorry but this script only runs on Windows.")


def getLocalUsers(): 
    print("\nGet local users on Windows.\n")

    try: 
        checkOsForWindows()
        
        startDateTime = datetime.now()
        print("Started getting local users at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('net user') != 0: 
            raise Exception("Error occurred while getting local users.")

        print(Fore.GREEN + "Successfully got local users." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting local users at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get local users." + Style.RESET_ALL)
        traceback.print_exc()
        exit("" + Style.RESET_ALL)

    
getLocalUsers()
