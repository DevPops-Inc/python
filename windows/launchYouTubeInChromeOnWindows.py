#!/bin/python

# launch YouTube in Chrome on Windows 

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
    print("Started checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    winPrograms = os.popen('PowerShell "Get-ItemProperty HKLM:\\Software\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\* | ForEach-Object {$_.DisplayName}"').read()

    if "Google Chrome" in winPrograms: 
        print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

        print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Google Chrome is not installed." + Style.RESET_ALL)

        print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def launchYouTubeInChrome(): 
    print("\nLaunch YouTube in Chrome on Windows.\n")
    
    checkOsForWindows()
    checkChrome()

    try: 
        startDateTime = datetime.now()
        print("Started launching YouTube at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        youTubeInChrome = 'start chrome "http://youtube.com"'
        
        if os.system(youTubeInChrome) != 0: 
            raise Exception("Error occurred when launching YouTube in Chrome.")
            
        print(Fore.GREEN + "Successfully launched YouTube in Chrome." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished launching YouTube at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to launch YouTube in Chrome.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


launchYouTubeInChrome()        
