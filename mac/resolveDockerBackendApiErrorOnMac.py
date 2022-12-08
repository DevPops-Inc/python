#!/bin/python

# resolve Docker failed to ping backend API error on Mac

# you can run this script with: python3 resolveDockerBackendApiErrorOnMac.py < process ID >

import colorama, os, subprocess, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

        
def checkDocker(): 
    print("Started checking Docker at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    FNULL = open(os.devnull, 'w')
    checkDockerOnMac = subprocess.call(['which', 'docker'], stdout=FNULL)

    if checkDockerOnMac == 0: 
        print(Fore.GREEN + "Docker is installed." + Style.RESET_ALL)
        os.system('docker --version')

        print("Finished checking Docker at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.GREEN + "Docker is not installed." + Style.RESET_ALL)

        print("Finished checking Docker at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def getDockerProcessId(): 
    print("Please press the \"control\" and \"C\" keys to return to the script after you find Docker's process ID.")

    print("")

    time.sleep(1)
    os.system('top | grep "Docker"')

    processId = str(input("Please type the process ID for Docker and press the \"return\" key (Example: 599): "))

    print("")
    return processId


def checkParameters(processId): 
    print("Started checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    valid = "true"

    print("Parameter(s): ")
    print("--------------------------------")
    print("processId: {0}".format(processId))
    print("--------------------------------")

    if processId == None: 
        print(Fore.RED + "processId is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)
        
        print("Finished checking parameter(s) at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def stopAndRestartDocker(processId): 
    print("Started stopping and restarting Docker at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    stopDocker = "kill {0}".format(processId)
    os.system(stopDocker)
    os.system('open -a Docker.app')
    print(Fore.GREEN + "Successsfully stopped and restarted Docker." + Style.RESET_ALL)

    print("Finished stopping and restarting Docker at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")


def resolveDockerBackendApiError(): 
    print("\nResolve Docker failed to ping backend API error on Mac.\n")

    checkOsForMac()
    checkDocker()

    if len(sys.argv) >= 2: 
        processId = str(sys.argv[1])

    else: 
        processId = getDockerProcessId()

    checkParameters(processId)

    try: 
        startDateTime = datetime.now()
        
        print("Started resolving Docker backend API error at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        stopAndRestartDocker(processId)
        print(Fore.GREEN + "Successfully resolved Docker backend API error." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished resolving Docker backend API error at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to resolve Docker backend API error.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


resolveDockerBackendApiError()
