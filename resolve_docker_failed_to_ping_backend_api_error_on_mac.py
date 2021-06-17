#!/bin/python

# resolve Docker failed to ping backend API error on Mac

import os

# prompt user input
str(input("\nResolve Docker failed to ping backend API error on Mac.\nPress any key to continue or press control and C keys to quit.\n"))

def getDockerProcessId(): 
    print("\nPlease press control and C keys to stop process after you find Docker's process ID.\n\n")
    os.system('top | grep "Docker"')

def stopAndRestartDocker():
    processId = str(input("\nPlease type the process ID for Docker (Example: 599): \n"))
    stopDocker = "kill {0}".format(processId)
    os.system(stopDocker)
    os.system('open -a Docker.app')

def resolveDockerFailedPingBackendApiError(): 
    getDockerProcessId
    stopAndRestartDocker

resolveDockerFailedPingBackendApiError
