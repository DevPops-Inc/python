#!/bin/python

# check youtube-dl in Python 

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


def checkYouTubeDl(): 
    print("\nCheck youtube-dl in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking youtube-dl at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkYouTubeDlOnMacOrLinux = subprocess.call(['which', 'youtube-dl'], stdout=FNULL) 

            if checkYouTubeDlOnMacOrLinux == 0:
                print(Fore.GREEN + "youtube-dl is installed."+ Style.RESET_ALL)
                os.system('youtube-dl --version')
                print(Fore.GREEN + "Successfully checked youtube-dl." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking youtube-dl at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "YouTubeDl is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking youtube-dl at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkYouTubeDlOnWindows = subprocess.call(['where', 'youtube-dl'], stdout=FNULL)

            if checkYouTubeDlOnWindows == 0:
                print(Fore.GREEN + "youtube-dl is installed."+ Style.RESET_ALL)
                os.system('youtube-dl --version')
                print(Fore.GREEN + "Successfully checked youtube-dl." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking youtube-dl at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "youtube-dl is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking youtube-dl at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception as e: 
        print(Fore.RED + "Failed to check youtube-dl in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkYouTubeDl()
