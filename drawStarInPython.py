#!/bin/python

# draw a star with turtle

# you can run this script with: python3 drawStarInPython.py < border color > < inside color >

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from turtle import *
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


def getBorderColor(operatingSystem): 
    if operatingSystem == "Windows": 
        borderColor = str(input("Please type the border color of the star and press the \"Enter\" key (Example: orange): "))

        print("")

    else: 
        borderColor = str(input("Please type the border color of the star and press the \"return\" key (Example: orange): "))

        print("")

    return borderColor


def getInsideColor(operatingSystem): 
    if operatingSystem == "Windows": 
        insideColor = str(input("Please type the inside color of the star and press the \"Enter\" key (Example: yellow): "))

        print("")

    else: 
        insideColor = str(input("Please type the inside color of the star and press the \"return\" key (Example: yellow): "))

        print("")

    return insideColor


def checkParameters(borderColor, insideColor): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = "true"

    print("Parameter(s): ")
    print("------------------------------------")
    print("borderColor: {0}".format(borderColor))
    print("insideColor: {0}".format(insideColor))
    print("------------------------------------")

    if borderColor == None: 
        print(Fore.RED + "borderColor is not set." + Style.RESET_ALL)
        valid = "false"

    if insideColor == None: 
        print(Fore.RED + "insideColor is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def drawStar(): 
    print("\nLet's draw a star in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        borderColor = str(sys.argv[1])
        insideColor = str(sys.argv[2])

    else: 
        borderColor = getBorderColor(operatingSystem)
        insideColor = getInsideColor(operatingSystem)

    checkParameters(borderColor, insideColor)

    try: 
        startDateTime = datetime.now()
        print("Started drawing star at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        color(borderColor, insideColor)

        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
        end_fill()
        done()

        print(Fore.GREEN + "Successfully drew star in Python." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished drawing star at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to draw star.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


drawStar()
