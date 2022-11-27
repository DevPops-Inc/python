#!/bin/python

# get local admin password expiration policy on Windows 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def getLocalAdminPwExpPolicy(): 
    print("\nGet local admin password expiration policy on Windows.\n")
    checkOsForWindows() 

    try: 
        startDateTime = datetime.now()
        print("Started getting local admin password expiration policy at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        os.system('net user administrator | findstr /C:expires')
        print(Fore.GREEN + "Successfuly got local admin expiration policy." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting local admin password expiration policy at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to get local admin password expiration policy.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getLocalAdminPwExpPolicy()
