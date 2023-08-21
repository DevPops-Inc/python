#!/bin/python

# set local admin password on Windows 

# run this script as administrator
# you can run this script with: python3 setLocalAdminPwOnWindows.py < local admin password >

import colorama, getpass, os, sys, traceback
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


def getAdminPw(): 
    adminPw = getpass.getpass("Please type the local admin default password and press the \"Enter\" key (Example: Password123): ")

    print("")
    return adminPw


def checkParameters(adminPw): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------")
    print("adminPw: {0}".format("***"))
    print("--------------------------")

    if adminPw == None or adminPw == "": 
        print(Fore.RED + "adminPw is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def setLocalAdminPw(): 
    print("\nSet local admin default password on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) >= 2: 
        adminPw = str(sys.argv[1])

    else: 
        adminPw = getAdminPw()

    checkParameters(adminPw)

    try: 
        startDateTime = datetime.now()
        
        print("Started setting local admin password at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        setAdminPw = 'net user administrator {0}'.format(adminPw)

        if os.system(setAdminPw) != 0: 
            raise("Error occurred while setting local admin password.")
        
        print(Fore.GREEN + "Successfully set local admin password." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished setting local admin password at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} seconds".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to set local admin password.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)

setLocalAdminPw()
