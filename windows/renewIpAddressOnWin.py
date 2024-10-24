#!/bin/python

# renew IP address on Windows 

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


def renewIpAddress(): 
    print("\nRenew IP address on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started renewing IP address at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('ipconfig /renew') != 0: 
            raise Exception("Error occurred while renewing IP address.")

        print(Fore.GREEN + "Successfully renewed IP address." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished renewing IP address at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to renew IP address.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


renewIpAddress()
        