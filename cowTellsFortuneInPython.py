#!/bin/python

# cow tells fortune in Python

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


def checkFortune(operatingSystem): 
    print("Started checking Fortune at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    FNULL = open(os.devnull,  'w')

    if operatingSystem == "Windows": 

        checkFortuneOnWindows = subprocess.call(['where', 'fortune'], stdout=FNULL)

        if checkFortuneOnWindows == 0: 
            print(Fore.GREEN + "Fortune in installed" + Style.RESET_ALL)

            print("Finished checking Fortune at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")
        
        else: 
            print(Fore.RED + "Fortune is not installed" + Style.RESET_ALL)

            print("Finished checking Fortune at", datetime.now().strfime("%m-%d-%Y %I:%M %p"))
            exit("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 

        checkFortuneOnMacOrLinux = subprocess.call(['which', 'fortune'], stdout=FNULL) 

        if checkFortuneOnMacOrLinux == 0: 
            print(Fore.GREEN + "Fortune is installed" + Style.RESET_ALL)

            print("Finished checking Fortune at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Fortuen is not installed." + Style.RESET_ALL)

            print("Finished checking Fortune at", datetime.now().strftime("%Y"))
            exit("")


def checkCowsay(operatingSystem):
    print("Started checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    FNULL = open(os.devnull,  'w')
    
    if operatingSystem == "Windows": 
        checkCowsayOnWindows = subprocess.call(['where', 'cowsay'], stdout=FNULL)

        if checkCowsayOnWindows == 0: 
            print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)

            print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)

            print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            exit("")

    if operatingSystem == "macOS" or operatingSystem == "Linux": 
        checkCowsayOnMacOrLinux = subprocess.call(['which', 'cowsay'], stdout=FNULL)

        if checkCowsayOnMacOrLinux == 0: 
            print(Fore.GREEN + "Cowsay is installed." + Style.RESET_ALL)

            print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)

            print("Finished checking Cowsay at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            exit("")


def cowTellsFortune():
    print("\nCow tell fortune in Python.\n")    
    
    operatingSystem = checkOs()
    checkFortune(operatingSystem)
    checkCowsay(operatingSystem)

    try: 
        startDateTime = datetime.now()
        print("Cow started telling fortune at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        os.system('fortune | cowsay')
        print(Fore.GREEN + "Cowsay successfully told fortune." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Cow finished telling fortune at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Cow failed to tell fortune." + Style.RESET_ALL)
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


cowTellsFortune()
