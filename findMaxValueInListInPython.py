#!/bin/python

# find maximum value in list recursively in Python

import colorama, os,sys, traceback
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
        print(Fore.GREEN + "Operating System: ", end="")
        os.system("uname -r")
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def findMaxValue(items):
    if len(items) == 1:
        return items[0]

    option1 = items[0]
    option2 = findMaxValue(items[1:])

    if option1 > option2:
        return option1
    else:
        return option2


def findMaxValueinList(): 
    print("\nLet's find the maximum value in a list in Python!\n")

    try: 
        operatingSystem = checkOs()
        
        startDateTime = datetime.now()
        print("Started finding maximum value in list at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        items = []

        if operatingSystem == "Windows": 
            itemList = int(input("Please type the number of items in your list and press the \"Enter\" key (Example: 10): "))

            print("")

            def addItemToListOnWin(itemList): 
                if itemList > 0: 
                    addItem = int(input("Please type a number you wish to add to the list and press the \"Enter\" key (Example: 25): "))

                    print("")
                    items.append(addItem)
                    addItemToListOnWin(itemList-1)

            addItemToListOnWin(itemList)

        else: 
            itemList = int(input("Please type the number of items in your list and press the \"return\" key (Example: 10): "))

            print("")

            def addItemToListOnWin(itemList): 
                if itemList > 0: 
                    addItem = int(input("Please type a number you wish to add to the list and press the \"return\" key (Example: 25): "))

                    print("")
                    items.append(addItem)
                    addItemToListOnWin(itemList-1)

            addItemToListOnWin(itemList)

        print("Here are the items in your list: {0}".format(items))
        
        print(Fore.BLUE + "The maximum number in the list is: {0}".format(findMaxValue(items)))

        print(Fore.GREEN + "Successfully found maximum value in a list." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished finding maximum value in a list", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception:
        print(Fore.RED + "Failed to find maximum value in list.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


findMaxValueinList()
