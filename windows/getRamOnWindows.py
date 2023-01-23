#!/bin/python

# get RAM on Windows 

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


def getRam(): 
    print("\nGet RAM on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting RAM at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('wmic MEMORYCHIP get BankLabel,DeviceLocator,Capacity,Tag') != 0: 
            raise Exception("Attempt threw an error!")

        finishedDateTime = datetime.now()
        print("Finished getting RAM at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to get RAM." + Style.RESET_ALL)
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getRam()
