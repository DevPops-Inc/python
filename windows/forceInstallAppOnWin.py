#!/bin/python

# force install application on Windows

# you can run this script with: python3 forceInstallAppOnWin.py "< installer location >" "< installer name >"

# need to test this with an .msi file

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
from pathlib import Path
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.version('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        raise Exception("Sorry but this script only runs on Windows.")


def getInstallerLocation(): 
    installerLocation = str(input("Please type the location of the installler and press the \"Enter\" key (Example: C:\\Users\\%USERNAME%\\Downloads): "))

    installerLocation = os.path.expandvars(installerLocation)
    os.listdir(installerLocation)
    print("")
    return installerLocation


def getInstallerName(): 
    installerName = str(input("Please type the installer name and press the \"Enter\" key (Example: Docker Desktop Installer.exe): "))

    print("")
    return installerName


def checkParameters(installerLocation, installerName): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------------------------------")
    print("installerLocation: {0}".format(installerLocation))
    print("installerName    : {0}".format(installerName))
    print("------------------------------------------------")

    if installerLocation == None or installerLocation == "": 
        print(Fore.RED + "installerLocation is not set." + Style.RESET_ALL)
        valid = False

    if installerName == None or installerName == "": 
        print(Fore.RED + "installName is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def forceInstallApp(): 
    print("\nForce install application on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) >= 2: 
        installerLocation = str(sys.argv[1])
        installerName     = str(sys.argv[2])

    else: 
        installerLocation = getInstallerLocation()
        installerName     = getInstallerName()

    checkParameters(installerLocation, installerName)

    try: 
        startDateTime = datetime.now()
        
        print("Started force installing application at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        installerLocation = Path(installerLocation)

        if not os.path.exists(installerLocation): 
            raise Exception("Installer location is invalid.")

        os.chdir(installerLocation)
        forceInstall = '"{0}" -i GUI'.format(installerName) # msiexec "{0}" /i
            
        if os.system(forceInstall) != 0: 
            raise Exception("Error occurred during installiation of application.")
    
        print(Fore.GREEN + "Successfully force installed application." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished force installing application at", finishedDateTime.strtime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to force install application.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


forceInstallApp()
