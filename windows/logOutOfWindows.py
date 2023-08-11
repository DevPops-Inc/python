#!/bin/python

# log out of Windows

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
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def logOut(): 
    print("\nLog out of Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started logging out at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('logoff') != 0: 
            raise Exception("Error occurred while logging off.")

        print(Fore.GREEN + "Successfully logged out." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished logging out at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to log out.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


logOut()
