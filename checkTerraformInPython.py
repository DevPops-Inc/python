#!/bin/python

# check Terraform in Python 

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem


def checkTerraform(): 
    print("\nCheck Terraform in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        print("Started checking Terraform at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":
            checkTerraformOnMacOrLinux = subprocess.call(['which', 'terraform'], stdout=FNULL) 

            if checkTerraformOnMacOrLinux == 0:
                print(Fore.GREEN + "Terraform is installed."+ Style.RESET_ALL)
                os.system('terraform --version')
                print(Fore.GREEN + "Successfully checked terraform." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Terraform at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Terraform is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Terraform at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            checkTerraformOnWindows = subprocess.call(['where', 'terraform'], stdout=FNULL)

            if checkTerraformOnWindows == 0:
                print(Fore.GREEN + "Terraform is installed."+ Style.RESET_ALL)
                os.system('terraform --version')
                print(Fore.GREEN + "Successfully checked terraform." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Terraform at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Terraform is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Terraform at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception: 
        print(Fore.RED + "Failed to check Terraform in Python.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkTerraform()
