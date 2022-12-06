#!/bin/python

# check Steam Locomotive in Python 

import colorama, os, sys, subprocess, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ", end="")
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


def checkSteamLocomotive(): 
    print("\nCheck Steam Locomotive in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking Steam Locomotive at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkSteamLocomotiveOnMacOrLinux = subprocess.call(['which', 'sl'], stdout=FNULL) 

            if checkSteamLocomotiveOnMacOrLinux == 0:
                print(Fore.GREEN + "Steam Locomotive is installed."+ Style.RESET_ALL)
                print(Fore.BLUE + "Do you hear a train approaching?" + Style.RESET_ALL)
                time.sleep(3)
                os.system('sl')
                print(Fore.GREEN + "Successfully checked Steam Locomotive." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Steam Locomotive at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Steam Locomotive is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Steam Locomotive at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkSteamLocomotiveOnWindows = subprocess.call(['where', 'sl'], stdout=FNULL)

            if checkSteamLocomotiveOnWindows == 0:
                print(Fore.GREEN + "Steam Locomotive is installed."+ Style.RESET_ALL)
                print(Fore.BLUE + "Do you hear a train approaching?" + Style.RESET_ALL)
                time.sleep(3)
                os.system('sl')
                print(Fore.GREEN + "Successfully checked Steam Locomotive." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Steam Locomotive at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Steam Locomotive is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Steam Locomotive at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception as e: 
        print(Fore.RED + "Failed to check Steam Locomotive in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkSteamLocomotive()
