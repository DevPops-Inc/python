#!/bin/python

# launch Chrome on Windows or Mac

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
        print(Fore.GREEN + "Opearting System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    if operatingSystem == "Windows" or operatingSystem == "macOS": 
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows or Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")

    return operatingSystem


def checkChrome(operatingSystem): 
    print("Started checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if operatingSystem == "Windows": 
        winPrograms = os.popen('PowerShell "Get-ItemProperty HKLM:\\Software\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\* | ForEach-Object {$_.DisplayName}"').read()

        if "Google Chrome" in winPrograms: 
            print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

            print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Google Chrome is not installed." + Style.RESET_ALL)

            print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            exit("")

    elif operatingSystem == "macOS": 
        chromeInApps = os.system('open -Ra "Google Chrome.app"')

        if chromeInApps == 0:
            print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

            print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Chrome is not installed." + Style.RESET_ALL)

            print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            exit("")


def launchChrome(): 
    print("\nLaunch Chrome on Windows or Mac.\n")

    operatingSystem = checkOsForWinOrMac()
    checkChrome(operatingSystem)

    try: 
        startDateTime = datetime.now()
        print("Started launching Chrome at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if operatingSystem == "Windows": 
            if os.system('start chrome') != 0:
                raise Exception("Unable to launch Chrome on Windows.")

        elif operatingSystem == "macOS": 
            if os.system('open -a "Google Chrome"') != 0: 
                raise Exception("Unable to launch Chrome on Mac.")

        print(Fore.GREEN + "Successfully launched Chrome." + Style.RESET_ALL)

        finishedDateTime = datetime.now() 
        print("Finished launching Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to launch Chrome.")        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        

launchChrome()
