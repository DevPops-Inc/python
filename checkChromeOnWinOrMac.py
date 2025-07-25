#!/bin/python

# check Chrome on Windows or Mac

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWinOrMac(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    if operatingSystem == "Windows" or operatingSystem == "macOS": 
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")
        return operatingSystem

    else: 
        raise Exception("Sorry this script only runs on Windows or macOS.")


def checkChromeOnWinOrMac(): 
    print("\nCheck Chrome on Windows or Mac.\n")

    try:
        operatingSystem = checkOsForWinOrMac()
        
        startDateTime = datetime.now()
        print("Started checking Chrome at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if operatingSystem == "Windows": 
            winPrograms = os.popen('PowerShell "Get-ItemProperty HKLM:\\Software\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\* | ForEach-Object {$_.DisplayName}"').read()

            if "Google Chrome" in winPrograms: 
                print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

                finishedDateTime = datetime.now()
                print("Finished checking Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Chrome is not installed.")

        elif operatingSystem == "macOS":
            chromeInApps = os.system('open -Ra "Google Chrome.app"')

            if chromeInApps == 0:
                print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

                finishedDateTime = datetime.now()
                print("Finished checking Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Chrome is not installed.")

    except Exception: 
        print(Fore.RED + "Failed to check Chrome on Windows or Mac.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkChromeOnWinOrMac()
