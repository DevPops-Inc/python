#!/bin/python 

# check Outlook on Windows 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
from pathlib import PureWindowsPath
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


def checkOutlook():
    print("\nCheck Outlook on Mac.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started checking Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        outlookPath = PureWindowsPath("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")

        if os.path.exists(outlookPath) == True: 
            print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

            print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Outlook is not installed." + Style.RESET_ALL)

            print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            exit("")

    except Exception: 
        print(Fore.RED + "Failed to check Outlook.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkOutlook()
