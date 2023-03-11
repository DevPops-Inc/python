#!/bin/python 

# check disk and restart Windows

# run this script as administrator

from inspect import trace
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
        print(Fore.RED + "Sorry but this script only runs Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def checkDiskAndRestartWindows():
    print("\nCheck disk and restart Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()

        print("Started checking disk and restarting Windows at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        os.system('echo y | chkdsk /f/r c:')

        finishedDateTime = datetime.now()

        print("Finished checking disk and restarting Windows at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0}".format(duration.seconds))
        print("")

        print("Please save your documents and close applications.")
        str(input("Press any key to restart Windows."))
        os.system('shutdown /r /t 0')
        
    except Exception: 
        print(Fore.RED + "Failed to check disk and restart Windows.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkDiskAndRestartWindows()
