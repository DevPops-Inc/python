#!/bin/python

# check SSH status on Mac

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin":
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else:
        print(Fore.RED + "Sorry but this script only runs on macOS." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def checkSshStatus(): 
    print("\nCheck SSH status on Mac.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started checking SSH at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        os.system('sudo systemsetup -getremotelogin')
        print(Fore.GREEN + "Successfully checked SSH status." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished checking SSSh at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to check SSH status.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkSshStatus()
