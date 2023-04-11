#!/bin/python

# view connected servers on Windows 

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


def viewConnectedServers(): 
    print("View all connected servers on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started viewing all connected servers at", startDateTime.strftime("%m-%d-%Y %I:%M %p")) 

        if os.system('net view') != 0: 
            raise Exception("An error occurred when trying to view connected servers.")
        
        print(Fore.GREEN + "Successfully viewed all connect servers." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished viewing all connected servers at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime 
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to view all connected servers.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


viewConnectedServers()
