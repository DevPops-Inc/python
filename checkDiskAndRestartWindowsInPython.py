#!/bin/python 

# check disk and restart Windows

# run this script as administrator

from inspect import trace
import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        print(Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

def checkDiskAndRestartWindows():
    print("\nCheck disk and restart Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()

        print("Started checking disk and restarting Windows at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        os.system('echo y | chkdsk /f/r c:')

        finishedDateTime = datetime.now()

        print("Finished checking disk and restarting Windows at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0}".format(duration.seconds))
        print("")

        print("Please save your documents and close applications.")
        str(input("Press any key to restart Windows."))
        os.system('shutdown /r /t 0')
        
    except Exception as e: 
        print(Fore.RED + "Failed to check disk and restart Windows.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkDiskAndRestartWindows()
