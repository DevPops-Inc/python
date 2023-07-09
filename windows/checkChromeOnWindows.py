#!/bin/python

# check Chrome on Windows

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
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def checkChrome(): 
    print("\nCheck Chome on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started checking Chrome at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        winPrograms = os.popen('PowerShell "Get-ItemProperty HKLM:\\Software\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\* | ForEach-Object {$_.DisplayName}"').read()

        print("Windows programs: ")
        print(Fore.BLUE + winPrograms + Style.RESET_ALL)

        if "Google Chrome" in winPrograms: 
            print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "Google Chrome is not installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")

    except Exception: 
        print(Fore.RED + "Failed to check Chrome.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkChrome()
