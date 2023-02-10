#!/bin/python

# resolve missing network drives on Windows 

# haven't tested this script on a domain PC yet 

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


def resolveMissingNetworkDrives(): 
    print("\nResolve missing network drives on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started resolving missing network drives at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('GPUpdate /target:user /force') != 0: 
            raise Exception("Attempt threw an error!")

        print(Fore.GREEN + "Successfully resolved missing network drives." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished resolving missing network drives at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print(Fore.BLUE + "Please save your documents and close applications.")
        str(input("Press any key to restart computer."))
        print(Style.RESET_ALL)
        os.system('shutdown /r /t 0')

    except Exception: 
        print(Fore.RED + "Failed to resolve missing network drives.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


resolveMissingNetworkDrives()
