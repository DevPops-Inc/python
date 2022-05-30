#!/bin/bash

# install pgzero module with PIP on Mac

check_os_for_mac() {
    echo "Started checking operating system at $(date)"

    if [[ $OSTYPE == 'darwin'* ]]; then 
        tput setaf 2; echo -e "Operating system:\n$(sw_vers)"; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""
    else 
        tput setaf 1; echo "Sorry but this script only runs on Mac."; tput sgr0

        echo "Finished checking operatign system at $(date)"
        echo ""
    fi
}

check_pip() {
    echo "Started checking PIP at $(date)"

    which -s pip
    if [[ $? == 0 ]]; then 
        tput setaf 2; echo "PIP is installed."; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""
    else 
        tput setaf 1; echo "PIP is not installed."; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""

        exit 1
    fi
}

check_pgzero_module () {
    echo "Started checking pgzero module at $(date)"

    pip list | grep pgzero
    if [[ $? == 0 ]]; then 
        tput setaf 2; echo "pgzero is installed."; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""

        exit 0
    else 
        tput setaf 1; echo "pgzero is not installed."; tput sgr0

        echo "Finished checking operating system at $(date)"
        echo ""
    fi
}

install_pgzero_module_with_pip() {
    printf "\nInstall pgzero module with PIP on Mac.\n\n"

    check_os_for_mac
    check_pip
    check_pgzero_module

    start=$(date +%s)
    echo "Started installing pgero module at $(date)"

    pip install pgzero
    pip list | greg pgzero
    tput setaf 2; echo "Successfully installed pgzero module."; tput sgr0

    end=$(date +%s)
    echo "Finished installing pgzero module $(date)"

    duration=$(( $end - $start ))
    echo "Total execution time: $duration second(s)"
    echo ""
}

install_pgzero_module_with_pip
