#!/bin/python

# get programs on Windows 

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def getPrograms(): 
    print("\nGet Programs on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting programs at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        os.system('Powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName | Format-Table -Autosize"')

        print(Fore.GREEN + "Successfully got programs." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting programs at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to get programs.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getPrograms()
