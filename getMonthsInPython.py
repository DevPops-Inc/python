#!/bin/python

# get months in Python

import calendar, colorama, os, sys, time, traceback
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
        os.system('unrame -r')
        print(Style.RESET_ALL, end="")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def getMonths(): 
    print("\nLet's get months in Python!\n")
    checkOs()

    try:
        startDateTime = datetime.now()
        print("Started getting months in Python at", startDateTime.strftime("%m-%d-%Y %I:%M %p"), end="")

        for name in calendar.month_name:
            print(Fore.BLUE + name)
            time.sleep(.5)

        print(Fore.GREEN + "Successfully got months." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting months at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get months.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getMonths()
