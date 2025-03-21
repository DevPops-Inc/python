#!/bin/python

# get local admin password expiration policy on Windows 

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
        raise Exception(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)


def getLocalAdminExpirationPolicy(): 
    print("\nGet local admin password expiration policy on Windows.\n")

    try:
        checkOsForWindows()

        startDateTime = datetime.now()
        
        print("Started getting local admin password expiration policy at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.BLUE, end="")

        if os.system('net user administrator | findstr /C:expires') != 0:
            raise Exception("Error occurred while getting local admin password expiration policy.")
        
        print(Fore.GREEN + "Successfully got local admin password expiration policy." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finshed getting local admin password expiration policy at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get local admin password expiration policy.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getLocalAdminExpirationPolicy()
