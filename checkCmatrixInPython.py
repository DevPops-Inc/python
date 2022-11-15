#!/bin/python

# check cmatrix in Python 

import colorama, os, sys, subprocess, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

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

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def checkCmatrix(): 
    print("\nCheck cmatrix in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking cmatrix at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkCmatrixOnMacOrLinux = subprocess.call(['which', 'cmatrix'], stdout=FNULL) 

            if checkCmatrixOnMacOrLinux == 0:
                print(Fore.GREEN + "cmatrix is installed."+ Style.RESET_ALL)
                print("")

                print("Do you want to run cmatrix now?")
                answer = str(input("Please press \"Y\" or \"N\" and press \"return\" key: "))
                print("")

                if answer == "Y":
                    print("Press \"control\" and \"C\" keys when you're ready to quit cmatrix.")
                    time.sleep(3)
                    os.system('cmatrix')

                print(Fore.GREEN + "Successfully checked cmatrix." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking cmatrix at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "cmatrix is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking cmatrix at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkCmatrixOnWindows = subprocess.call(['where', 'cmatrix'], stdout=FNULL)

            if checkCmatrixOnWindows == 0:
                print(Fore.GREEN + "cmatrix is installed."+ Style.RESET_ALL)
                print("")

                print("Do you want to run cmatrix now?")
                answer = str(input("Please press \"Y\" or \"N\" and press \"Enter\" key: "))
                print("")

                if answer == "Y":
                    print("Press \"Ctrl\" and \"C\" keys when you're ready to quit cmatrix.")
                    time.sleep(3)
                    os.system('cmatrix')

                print(Fore.GREEN + "Successfully checked cmatrix." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking cmatrix at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "cmatrix is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking cmatrix at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception as e: 
        print(Fore.RED + "Failed to check cmatrix in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkCmatrix()
