#!/bin/bash

# install Pygame Module with PIP on Mac

check_os_for_mac() {
    echo "Started checking operating system at $(date)"

    if [[ $OSTYPE == 'darwin'* ]]; then 
        tput setaf 2; echo -e "Operating system:\n$(sw_vers)"; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""
    else
        tput setaf 1; echo "Sorry but this script only runs on Mac."; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""

        exit 1
    fi
}

check_pip() {
    echo "Started checking PIP at $(date)"

    which -s pip
    if [[ $? == 0 ]]; then 
        tput setaf 2; echo "PIP is installed."; tput sgr0
        pip --version 

        echo "Finished checking PIP at $(date)"
        echo ""
    else 
        tput setaf 1; echo "PIP is not installed."; tput sgr0

        echo "Finished checking PIP at $(date)"
        echo ""

        exit 1
    fi
}

check_pygame() {
    echo "Started checking pygame module at $(date)"

    pip list | grep pygame
    if [[ $? == 0 ]]; then 
        tput setaf 2; echo "pygame is installed."; tput sgr0

        echo "Finished checking pygame at $(date)"
        echo ""

        exit 0
    else 
        tput setaf 1; echo "pygame is not installed."; tput sgr0

        echo "Finished checking pygame at $(date)"
        echo ""
    fi
}

check_python3() {
    echo "Started checking Python 3 at $(date)"

    which -s python3
    if [[ $? == 0 ]]; then 
        tput setaf 2; echo "Python 3 is installed."; tput sgr0
        python3 --version 

        echo "Finished checking Python 3 at $(date)"
        echo ""
    else 
        tput setaf 1; echo "Python 3 is not installed."; tput sgr0

        echo "Finished checking Python 3 at $(date)"
        echo ""

        exit 1
    fi
}

install_pygame_with_pip() {
    printf "\nInstall pygame module with PIP on Mac.\n\n"

    check_os_for_mac
    check_pip
    check_pygame
    check_python3

    start=$(date +%s)
    echo "Started installing pygame module at $(date)"

    pip install pygame
    pip list | grep pygame
    tput setaf 2; echo "Successfully installed pygame module."; tput sgr0

    end=$(date +%s)
    echo "Finished installing pygame module at $(date)"

    duration=$(( $end - $start ))
    echo "Total execution time: $duration second(s)"
    echo ""
}

install_pygame_with_pip
