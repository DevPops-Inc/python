#!/bin/python 

# disable BitLocker on Windows 

# haven't tested this script on Windows yet

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


def disableBitLocker(): 
    print("\nDisable BitLocker on Windows.\n")

    try: 
        checkOsForWindows()
        
        startDateTime = datetime.now()
        print("Started disabling BitLocker at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
        
        if os.system('manage-bde -off C:') != 0: 
            raise Exception("Error occurred while disabling BitLocker.")

        print(Fore.GREEN + "Successfully disabled BitLocker." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished disabling BitLocker at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to disable BitLocker.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


disableBitLocker()
