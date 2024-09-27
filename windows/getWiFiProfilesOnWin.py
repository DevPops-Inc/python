#!/bin/python

# get Wi-Fi profiles on Windows 

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
        raise Exception("Sorry but this script only runs on Windows.")


def getWiFiProfiles(): 
    print("\nGet Wi-Fi profiles on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started getting Wi-Fi profiles at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('netsh wlan show profiles') != 0: 
            raise Exception("Error occurred while getting Wi-Fi profiles.")
            
        print(Fore.GREEN + "Successfully got Wi-Fi profiles." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished getting Wi-Fi profiles at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print("")

    except Exception: 
        print(Fore.RED + "Failed to get Wi-Fi profiles.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getWiFiProfiles()
