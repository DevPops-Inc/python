#!/bin/python

# systems file check on Windows 

# run this script as admin
# haven't tested this script yet

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
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")
        

def systemsFileCheck(): 
    print("\nSystems file check on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started systems file check at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('SFC /scannow') != 0: 
            raise Exception("Error occurred while starting systems file chedk.")
        
        print(Fore.GREEN + "Successfully ran systems file check." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished systems file check at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to run systems file check.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)

    
systemsFileCheck()
