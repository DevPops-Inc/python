#!/bin/python

# check programs on Windows

# you can run this script with: python3 checkProgramOnWindows.py '< program >' 

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
        

def getProgam(): 
    program = str(input("Please type the program to check and press the \"Enter\" key (Example: Google Chrome): "))

    print("")
    return program


def checkParameters(program): 
    print("Started checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    valid = "true"

    print("Parameters:")
    print("----------------------------")
    print("program: {0}".format(program))
    print("----------------------------")

    if program == None: 
        print(Fore.RED + "program is noet set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passsed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def checkProgram(): 
    print("\nCheck program on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) >= 2: 
        program = str(sys.argv[1])

    else: 
        program = getProgam()

    checkParameters(program)

    try: 
        startDateTime = datetime.now()
        
        print("Started checking {0} at {1}".format(program, startDateTime.strftime("%Y-%m-%d %H:%M %p")))

        winPrograms = os.popen('PowerShell "Get-ItemProperty HKLM:\\Software\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\* | ForEach-Object {$_.DisplayName}"').read()

        winPrograms2 = os.popen('PowerShell "Get-WmiObject -Class Win32_Product | ForEach-Object {$_.Name}"').read()

        print("Windows programs: ")
        print(Fore.BLUE + winPrograms + winPrograms2 + Style.RESET_ALL)

        if program in winPrograms or program in winPrograms2: 
            print(Fore.GREEN + "{0} is installed.".format(program) + Style.RESET_ALL)
    
            finishedDateTime = datetime.now()

            print("Finished checking {0} at {1}".format(program, finishedDateTime.strftime("%Y-%m-%d %H:%M %p")))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "{0} is not installed.".format(program) + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            
            print("Finished checking {0} at {1}".format(program, finishedDateTime.strftime("%Y-%m-%d %H:%M %p")))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")

    except Exception as e: 
        print(Fore.RED + "Failed to check {0}.".format(program))
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkProgram()
