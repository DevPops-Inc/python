#!/bin/python 

# get network connections on Windows 

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


def getNetworkConnections(): 
    print("\nGet network connections on Windows.\n")

    try: 
        checkOsForWindows()
        
        startDateTime = datetime.now()
        
        print("Started getting network connections at", startDateTime.strftime("%m-%d-%Y %I:M %p"))

        if os.system('ipconfig /all') != 0: 
            raise Exception("Error occurred while getting network connections.")

        print("")
        print(Fore.GREEN + "Successfully got network connections." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished getting network connections at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print("Failed to get network connections.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getNetworkConnections()
