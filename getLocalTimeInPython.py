#!/bin/python

# get local time

import colorama, os, sys, time, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "darwin":
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def getLocalTime():
    print("\nGet local time in Python.\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        print("Started getting local time at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.BLUE + "The local time is: {0}".format(time.asctime()))
        print(Fore.GREEN + "Successfully got local time." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting local time at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total executime time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get local time.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getLocalTime()
