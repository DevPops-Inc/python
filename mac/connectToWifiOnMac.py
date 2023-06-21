#!/bin/python

# connect to Wi-Fi on Mac

# you can run this script with: python3 connectToWifiOnMac.py < SSID > < password >

import colorama, getpass, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")
    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def getWifiSsid(): 
    wifiSsid = str(input("Please type the SSID of the Wi-Fi network you wish to connect to and press \"return\" key (Example: Starbucks): "))

    print("")
    return wifiSsid


def getWifiPassword(): 
    wifiPassword = getpass.getpass("Please type the password for the Wi-Fi network you wish to connect to and press \"return\" key (Example: Password123): ")

    print("")
    return wifiPassword


def checkParameters(wifiSsid, wifiPassword): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("----------------------------------")
    print("wifiSsid    : {0}".format(wifiSsid))
    print("wifiPassword: {0}".format("***"))
    print("----------------------------------")

    if wifiSsid == None or wifiSsid == "": 
        print(Fore.RED + "wifiSsid is not set." + Style.RESET_ALL)
        valid = False

    if wifiPassword == None or wifiPassword == "":
        print(Fore.RED + "wifiPassword is not set." + Style.RESET_ALL)
        valid = False

    if valid == True:
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect.", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def connectToWifi(): 
    print("\nConnect to Wi-Fi on Mac.\n")
    checkOsForMac()

    if len(sys.argv) > 2:
        wifiSsid     = str(sys.argv[1])
        wifiPassword = str(sys.argv[2])

    else: 
        wifiSsid     = getWifiSsid()
        wifiPassword = getWifiPassword()

    checkParameters(wifiSsid, wifiPassword)

    try: 
        startDateTime = datetime.now()

        print("Started connecting to {0} at {1}".format(wifiSsid, startDateTime.strftime("%m-%d-%Y %I:%M %p")))
        
        connectToWifi = "networksetup -setairportnetwork en0 {0} {1}".format(wifiSsid, wifiPassword)

        if os.system(connectToWifi) != 0: # TODO: figure out exception handling
            raise Exception("Attempt threw an error!")

        print(Fore.GREEN + "Successfully connected to {0}".format(wifiSsid) + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished connecting to {0} at {1}".format(wifiSsid, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to connect to {0}".format(wifiSsid))
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
    
        
connectToWifi()
