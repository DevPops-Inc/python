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
        raise Exception("Sorry but this script only runs Windows.")


def checkDiskAndRestartWindows():
    print("\nCheck disk and restart Windows.\n")

    try: 
        checkOsForWindows()
        
        startDateTime = datetime.now()

        print("Started checking disk and restarting Windows at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('echo y | chkdsk /f/r c:') != 0: 
            raise Exception("Error occurred while initializing check disk.")

        finishedDateTime = datetime.now()

        print("Finished checking disk and restarting Windows at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0}".format(duration.seconds))
        print("")

        print("Please save your documents and close applications.")
        str(input("Press any key to restart Windows."))
        
        if os.system('shutdown /r /t 0') != 0: 
            raise Exception("Error occurred while restarting computer.")
        
    except Exception: 
        print(Fore.RED + "Failed to check disk and restart Windows.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkDiskAndRestartWindows()
