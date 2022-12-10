#!/bin/python 

# change local user password on Windows 

# you can run this script with changeLocalUserPasswordOnWindows.py < new password >

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
    print("Checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System: ", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        
    else:
        print(Fore.RED + "Sorry this script only works on Windows." + Style.RESET_ALL)
    
    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")

def getnewPassword(): # find way to obfuscate password
    newPassword = str(input("Please type your new password and press \"Enter\" key: (Example: Password123)"))

    print("")
    return newPassword


def checkParameters(newPassword):
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    valid = "true"

    print("Parameter(s):")
    print("------------------------------")
    print("newPassword: {0}".format("***"))
    print("------------------------------")

    if newPassword == None: 
        print(Fore.RED + "newPassword is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")
    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def changeLocalUserPassword():
    print("\nChange local user password on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) > 2:
        newPassword = str(sys.argv[1])
    else: 
        newPassword = getnewPassword()    
    
    try: 
        startDateTime = datetime.now()
        print("Started changing local user password at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
        setPassword = "SET localuser = {0}".format(newPassword)
        os.system(setPassword)
        os.system('net user %localuser% *')
        print(Fore.GREEN + "Successfully changed local user password." + Style.RESET_ALL)
		
        finishedDateTime = datetime.now()
		
        print("Finished changed local user password at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
		
        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e:
        print(Fore.RED + "Failed to change local user password.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
		
		
checkOsForWindows()
