#!/bin/python 

# get network connections on Windows 

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


def getNetworkConnections(): 
    print("\nGet network connections on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started getting network connections at", startDateTime.strftime("%m-%d-%Y %I:M %p"))

        if os.system('ipconfig /all') != 0: 
            raise Exception("Attempt threw an error!")

        print("")
        print(Fore.GREEN + "Successfully got network connections." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished getting network connections at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print("Failed to get network connections.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getNetworkConnections()
