#!/bin/python

# get printers on Windows 

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


def getPrinter(): 
    print("\nGet printers on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting printers at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.BLUE)

        if os.system('wmic printer get name /value') != 0: 
            raise Exception("Attempt threw an error!")

        print(Fore.GREEN + "Successfully got printers." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting printers at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total exectuion time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get printers.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getPrinter()
    