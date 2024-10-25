#!/bin/python

# resolve Windows updates issues

# run this script as admin

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


def resolveWinUpdates(): 
    print("\nResolve Windows updates issues.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started resolving Windows updates issues at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        os.chdir('/Windows')
        
        if os.system('echo y | del "SoftwareDistribution"') != 0:
            raise Exception("Error occurred while resolving Windows updates issues.")

        print(Fore.GREEN + "Successfully resolved Windows updates issues." + Style.RESET_ALL)

        finisheDateTime = datetime.now()
        
        print("Finished resolving Windows updates issues at", finisheDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finisheDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print(Fore.BLUE + "Please save documents and close applications.")
        input("Press any key to restart Windows:")
        print(Style.RESET_ALL)
        
        if os.system('shutdown /r /t 0') != 0:
            raise Exception("Error occurred while shutting down.")

    except Exception: 
        print(Fore.RED + "Failed to resolve Windows updates issues.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


resolveWinUpdates()
