#!/bin/python

# force group policy on Windows 

# haven't tested this script on a domain PC

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


def forceGroupPolicy(): 
    print("\nForce group policy on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started forcing group policy at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
        
        if os.system('gpudate /force') != 0: 
            raise Exception("Error occurred while forcing group policy.")

        print(Fore.GREEN + "Successfully forced group policy." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished forcing group policy at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to force group policy.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


forceGroupPolicy()
