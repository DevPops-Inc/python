#!/bin/python

# get local user password expiration policy on Windows 

# you can run this script with: python3 getLocalUserPwExpPolicyOnWindows.py "< local user >"

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


def getLocalUser(): 
    localUser = str(input("Please type the local user you want password expiration for and press the \"Enter\" key (Example: local.user): "))

    print("")
    return localUser


def checkParameters(localUser): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-$Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------------")
    print("localUser: {0}".format(localUser))
    print("--------------------------------")

    if localUser == None or localUser == "": 
        print(Fore.RED + "localUser is not set.")
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def getLocalUserPwExpPolicy(): 
    print("\nGet local user password expiration policy on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) >= 2: 
        localUser = str(sys.argv[1])

    else: 
        localUser = getLocalUser()

    checkParameters(localUser)

    try:
        startDateTime = datetime.now()
        
        print("Started getting \"{0}\" password expiration policy at {1}".format(localUser, startDateTime.strftime("%m-%d-%Y %I:%M %p")))

        pwExpPolicy = 'net user "{0}" | findstr /C:expires'.format(localUser)
        print(Fore.BLUE, end=""); sys.stdout.flush()

        if os.system(pwExpPolicy) != 0:
            raise Exception("Error occurred while getting local user password expiration policy.")
        
        print(Fore.GREEN + "Successfully got \"{0}\" password expiration policy.".format(localUser) + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finshed getting \"{0}\" password expiration policy at {1}".format(localUser, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get \"{0}\" password expiration policy.".format(localUser))
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getLocalUserPwExpPolicy()
