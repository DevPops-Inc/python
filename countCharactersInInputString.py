#!/bin/python

# count characters in input string

# you can run this script with: python3 countCharactersInInputString.py < input string >

import traceback
import colorama, os, sys 
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System")
        print(os.system('ver'))
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem

def getInputString(operatingSystem): 
    if operatingSystem == "Windows": 
        inputString = str(input("Please type something you want the character count for and press \"Enter\" key (Example: ham sandwich): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        inputString = str(input("Please type something you want the character count for and press \"return\" key (Example: ham sandwich): "))

        print("")

    return inputString

def checkParameters(inputString): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
    print("------------------------------------")
    print("inputString: {0}".format(inputString))
    print("------------------------------------")

    if inputString == None: 
        print(Fore.RED + "inputString is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("Y-%m-%d %H:%M %p"))

        exit("")

def countCharacters(): 
    print("\nCount characters in input string.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        inputString = str(sys.argv[1])
    else: 
        inputString = getInputString(operatingSystem)

    checkParameters(inputString)

    try: 
        startDateTime = datetime.now()

        print("Started counting characters at", startDateTime.strftime("%Y-%M-%d %H:%M %p"))

        characterCount = len(inputString)
        print(Fore.BLUE + "The string has {0} characters.".format(characterCount))
        
        print(Fore.GREEN + "Successfully counted characters in input string." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished counting characters at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0}".format(duration.seconds))
        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to count characters in string.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

countCharacters()
