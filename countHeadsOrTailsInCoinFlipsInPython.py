#!/bin/python

# count heads or tails in coin flips in Python

# you can run this script with: python3 countHeadsOrTailsInCoinFlipsInPython.py < number of coin flips > 

import colorama, random, os, sys, traceback
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

    
def getCoinFlips(operatingSystem):
    if operatingSystem == "Windows": 
        coinFlip = int(input("Please type the number of coin flips you would like and press \"Enter\" key (Example: 5): "))

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        coinFlip = int(input("Please type the number of coin flips you would like and press \"return\" key (Example: 5): "))

    print("")
    return coinFlip


def checkParameters(coinFlip): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------------")
    print("coinFlip: {0}".format(coinFlip))
    print("------------------------------")

    if coinFlip == None or coinFlip == "": 
        print(Fore.RED + "coinFlip is not set." + Style.RESET_ALL)
        valid = False
    
    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")

    
def countHeadsOrTailsInCoinFlips(): 
    print("\nLet's count heads or tails in coin flips!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        coinFlip = int(sys.argv[1])

    else: 
        coinFlip = getCoinFlips(operatingSystem)

    checkParameters(coinFlip)

    try: 
        startDateTime = datetime.now()

        print("Started counting heads and tails in coin flips at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        output = {"Heads":0, "Tails":0}
        coin   = list(output.keys())

        for i in range(coinFlip):
            output[random.choice(coin)]+=1

        print("The results of the coin flips are:" + Fore.BLUE)
        print("Heads:", output["Heads"])
        print("Tails:", output["Tails"])
        print(Fore.GREEN + "Successfully counted heads and tails in coin flip." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished counting heads and tails in coin flips at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to count heads and tails in coin flips.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


countHeadsOrTailsInCoinFlips()
