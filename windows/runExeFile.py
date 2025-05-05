#!/bin/python

# run exe file

# you can run this script with: python3 runExeFile.py "< .exe file location >" "< .exe filename >"

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
from pathlib import PureWindowsPath
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


def getExeFileLocation(): 

    exeFileLocation = str(input("Please type the location of the .exe file you want to run and press the \"Enter\" key (Example: C:\\Users\\%USERNAME%\\Downloads): "))

    exeFileLocation = os.path.expandvars(exeFileLocation)
    print("")
    return exeFileLocation


def getExeFileName(): 

    exeFilename = str(input("Please type the filename of the .exe and press the \"Enter\" key (Example: Docker Desktop Installer.exe): "))

    print("")
    return exeFilename


def checkParameters(exeFileLocation, exeFilename): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------------------------------")
    print("exeFileLocation: {0}".format(exeFileLocation))
    print("exeFilename    : {0}".format(exeFilename))
    print("------------------------------------------------")

    if exeFileLocation == None or exeFileLocation == "": 
        print(Fore.RED + "exeFileLocation is not set." + Style.RESET_ALL)
        valid = False

    if exeFilename == None or exeFileLocation == "": 
        print(Fore.RED + "installName is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def runExeFile(): 
    print("\nRun .exe file.\n")

    try: 
        checkOsForWindows()

        if len(sys.argv) >= 2: 
            exeFileLocation = str(sys.argv[1])
            exeFilename     = str(sys.argv[2])

        else: 
            exeFileLocation = getExeFileLocation()
            exeFilename     = getExeFileName()

        checkParameters(exeFileLocation, exeFilename)

        startDateTime = datetime.now()
        
        print("Started running .exe file at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        exeFilename = PureWindowsPath(exeFileLocation, exeFilename)
        runExe = '"{0}"'.format(exeFilename) 
        
        if os.system(runExe) != 0: 
            raise Exception("Error occurred while running .exe file.")

        print(Fore.GREEN + "Successfully ran .exe file." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished running .exe file at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to run .exe file.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


runExeFile()
