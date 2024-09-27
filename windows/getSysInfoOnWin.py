#!/bin/python

# get system information on Windows

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsFoWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        raise Exception("Sorry but this script only runs on Mac.")


def getSystemInfo(): 
    print("\nGet system information on Windows.\n")
    checkOsFoWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started getting system information at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('systeminfo') != 0: 
            raise Exception("Error occurred when getting system information.")

        print(Fore.GREEN + "Successfully got system information." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting system information at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get system information.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getSystemInfo()
