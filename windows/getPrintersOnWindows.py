#!/bin/python

# get printers on Windows 

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


def getPrinter(): 
    print("\nGet printers on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting printers at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        # getPrinters = ['wmic printer get name /value', 'cmd /k']
        # print(Fore.BLUE)

        # for printer in getPrinters:
        #     if os.system(printer) != 0: 
        #         raise Exception("Attempt threw an error!")

        os.system('wmic printer get name /value')
        print(Fore.GREEN + "Successfully got printers." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting printers at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total exectuion time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to get printers.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getPrinter()
    