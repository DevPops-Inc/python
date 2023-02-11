#!/bin/python

# draw a square in Python

# you can run this script with: python3 drawSquareInPython.py < border color > < fill color > 

import colorama, os, sys, turtle, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print("Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print("Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print("Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finisehd checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))
    print("")
    return operatingSystem


def getBorderColor(operatingSystem):
    if operatingSystem == "Windows": 
        borderColor = str(input("Please type the border color for the square and press the \"Enter\" key (Example: red): "))

    else: 
        borderColor = str(input("Please type the border color for the square and press the \"return\" key (Example: red): "))

    print("")
    return borderColor


def getFillColor(operatingSystem): 
    if operatingSystem == "Windows": 
        fillColor = str(input("Please type the fill color for the square and press the \"Enter\" key (Example: yellow): "))

    else: 
        fillColor = str(input("Please type the fill color for the square and press the \"return\" key (Example: yellow): "))

    print("")
    return fillColor


def checkParameters(borderColor, fillColor): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = "true"

    print("Parameter(s): ")
    print("------------------------------------")
    print("borderColor: {0}".format(borderColor))
    print("fillColor  : {0}".format(fillColor))
    print("------------------------------------")

    if borderColor == None: 
        print(Fore.RED + "borderColor is not set." + Style.RESET_ALL)
        valid = "false"

    if fillColor == None: 
        print(Fore.RED + "fillColor is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def drawSquare(): 
    print("\nLet's draw a square in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) > 2: 
        borderColor = str(sys.argv[1])
        fillColor   = str(sys.argv[2])

    else: 
        borderColor = getBorderColor(operatingSystem)
        fillColor   = getFillColor(operatingSystem)

    checkParameters(borderColor, fillColor)

    try: 
        startDateTime = datetime.now()
        print("Started drawing square at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        turtle.color(borderColor, fillColor)
        turtle.shape("turtle")

        turtle.begin_fill()
        for t in range(4): 
            turtle.forward(100)
            turtle.left(90)
        turtle.end_fill()
        turtle.getscreen()._root.mainloop()
        print(Fore.GREEN + "Successfully drew square in Python." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished drawing square at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to draw square.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


drawSquare()
