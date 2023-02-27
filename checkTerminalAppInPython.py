#!/bin/python

# check terminal application in Python 

# you can run this script with: python3 checkTerminalAppInPython.py < terminal app >

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def getTerminalApp(operatingSystem):
    if operatingSystem == "Windows": 
        terminalApp = str(input("Please type the terminal application you wish to check and press \"Enter\" key (Example: terraform): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        terminalApp = str(input("Please type the terminal application you wish to check and press \"return\" key (Example: terraform): "))

        print("")

    return terminalApp


def checkParameters(terminalApp):
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    valid = True

    print("Parameter(s):")
    print("------------------------------------")
    print("terminalApp: {0}".format(terminalApp))
    print("------------------------------------")

    if terminalApp == None: 
        print(Fore.RED + "terminalApp is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect" + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def checkTerminalApp(): 
    print("\nCheck terminal application in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        terminalApp = str(sys.argv[1])

    else: 
        terminalApp = getTerminalApp(operatingSystem)

    checkParameters(terminalApp)

    try:
        startDateTime = datetime.now()
        
        print("Started checking {0} at {1}".format(terminalApp, startDateTime.strftime("%m-%d-%Y %I:%M %p")))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkTerminalAppOnMacOrLinux = subprocess.call(['which', terminalApp], stdout=FNULL) 

            if checkTerminalAppOnMacOrLinux == 0:
                print(Fore.GREEN + "{0} is installed.".format(terminalApp) + Style.RESET_ALL)

                sanityCheck = "{0} --version".format(terminalApp)
                os.system(sanityCheck)

                print(Fore.GREEN + "Successfully checked {0}.".format(terminalApp) + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking {0} at".format(terminalApp), finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "{0} is not installed.".format(terminalApp) + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking {0} at".format(terminalApp), finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkTerminalAppOnWindows = subprocess.call(['where', terminalApp], stdout=FNULL)

            if checkTerminalAppOnWindows == 0:
                print(Fore.GREEN + "{0} is installed.".format(terminalApp) + Style.RESET_ALL)

                sanityCheck = "{0} --version".format(terminalApp)
                os.system(sanityCheck)

                print(Fore.GREEN + "Successfully checked {0}.".format(terminalApp) + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking {0} at".format(terminalApp), finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "{0} is not installed.".format(terminalApp) + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking {0} at".format(terminalApp), finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception: 
        print(Fore.RED + "Failed to check {0} in Python.".format(terminalApp))
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkTerminalApp()
