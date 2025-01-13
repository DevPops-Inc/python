#!/bin/python

# check four letter word in Python

# you can run this script with: python3 checkFourLetterWordInPython.py < four letter word >

import colorama, os, sys, traceback
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
        print(Fore.GREEN + "Operating System:")
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


def getFourLetterWord(operatingSystem): 
    if operatingSystem == "Windows": 
        fourLetterWord = str(input("Please type a four letter word and press the \"Enter\" key (Example: code): "))

    else: 
        fourLetterWord = str(input("Please type a four letter word and press the \"return\" key (Example: code): "))
        
    print("")    
    return fourLetterWord


def checkParameters(fourLetterWord): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("-----------------------------------------")
    print("fourLetteWord: {0}".format(fourLetterWord))
    print("-----------------------------------------")

    if fourLetterWord == None or fourLetterWord == "": 
        print(Fore.RED + "fourLetterWord is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def checkFourLetterWord():
    print("\nLet's check a four letter word in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        fourLetterWord = str(sys.argv[1])

    else: 
        fourLetterWord = getFourLetterWord(operatingSystem)

    try: 
        checkParameters(fourLetterWord)
        
        startDateTime = datetime.now()

        print("Started checking four letter word at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        wordLength = len(fourLetterWord)

        if wordLength == 4:
            print(Fore.BLUE + "\"{0}\" is a four letter word.".format(fourLetterWord.capitalize()) + Style.RESET_ALL)
            
        else:
            print(Fore.RED + "\"{0}\" is not a four letter word.".format(fourLetterWord.capitalize()) + Style.RESET_ALL)

        print(Fore.GREEN + "Successfully checked four letter word." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished checking four letter word at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to check four letter word.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkFourLetterWord()
