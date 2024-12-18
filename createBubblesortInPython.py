#!/bin/python

# create bubble sort in Python

import colorama, os, sys, time, traceback
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


def bubbleSort(dataset): 
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        time.sleep(.25)
    print(dataset)


def createBubblesort():
    print("\nLet's create a bubblesort in Python!\n")
    operatingSystem = checkOs()

    try: 
        startDateTime = datetime.now()    
        print("Started creating bubbleshort at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        list = []

        if operatingSystem == "Windows": 
            numList = int(input("Please type the number of items in your list and press the \"Enter\" key (Example: 10): "))

            print("")

            def addItemToListOnWin(numList): 
                if numList > 0: 
                    addItem = int(input("Please type a number you wish to add to the list and press the \"Enter\" key (Example: 25): "))

                    print("")

                    list.append(addItem)
                    addItemToListOnWin(numList-1)

            addItemToListOnWin(numList)

        else: 
            numList = int(input("Please type the number of items in your list and press the \"return\" key (Example: 10): "))

            print("")

            def addItemToListOnMacOrLinux(numList): 
                if numList > 0: 
                    addItem = int(input("Please type a number you wish to add to the list and press the \"return\" key (Example: 25): "))

                    print("")

                    list.append(addItem)
                    addItemToListOnMacOrLinux(numList-1)

            addItemToListOnMacOrLinux(numList)

            print(Fore.BLUE + "Here is your dataset:")
            print(list)
            print("Here is your bubblesort:")
            bubbleSort(list)
            print(Fore.GREEN + "Successfully created bubblesort." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished creating bubblesort at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

    except Exception: 
        print(Fore.RED + "Failed to create bubblesort.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


createBubblesort()
