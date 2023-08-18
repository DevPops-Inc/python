#!/bin/python

# restart Windows 

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
        print(Fore.RED + "Sorry but this script only runs on Windows.")
        
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def restartWin():
    print("\nRestart Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started restarting Windows at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.GREEN + "Successfully restarted Windows." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished restarting Windows at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print(Fore.BLUE + "Please save documents and close applications.")
        input("Press any key to restart Windows: ")
        print(Style.RESET_ALL)

        if os.system('shutdown /r /t 0') != 0: 
            raise Exception("Errorred occurred while restarting Windows.")

    except Exception: 
        print(Fore.RED + "Failed to restart Windows.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


restartWin()
