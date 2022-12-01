#!/bin/python

# get days of the week 

import calendar, colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")
    return operatingSystem


def getDaysOfWeek(): 
    print("\nLet's get the days of the week in Python!\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        print("Started getting the days of the week at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        week = [6, 0, 1, 2, 3, 4, 5]

        for day in week: 
            time.sleep(.5)
            print(Fore.BLUE + calendar.day_name[day])

        print(Fore.GREEN + "Successfully got the days of the week." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting the days of the week at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to get days of the week.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getDaysOfWeek()
    