#!/bin/python

# force install application on Windows

# you can run this script with: python3 forceInstallAppOnWindows.py "< installer location >" "< installer name >"

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
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
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


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
    valid = "true"

    print("Parameter(s):")
    print("------------------------------------------------")
    print("installerLocation: {0}".format(installerLocation))
    print("installerName    : {0}".format(installerName))
    print("------------------------------------------------")

    if installerLocation == None: 
        print(Fore.RED + "installerLocation is not set." + Style.RESET_ALL)
        valid = "false"

    if installerName == None: 
        print(Fore.RED + "installName is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


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

        os.chdir(installerLocation)
        forceInstall = "{0} -i GUI".format(installerName)
        
        if os.system(forceInstall) != 0: 
            raise Exception("Attempt threw an error!")

        print(Fore.GREEN + "Successfully force installed application." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished force installing application at", finishedDateTime.strtime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to force install application.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


forceInstallApp()
