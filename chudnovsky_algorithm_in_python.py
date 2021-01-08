#!/bin/python

# calculate the value of pi with Chudnovsky Algorithm

# import modules
from decimal import Decimal, getcontext
import math
import time
import colorama
from colorama import Fore
colorama.init()

# input decimal places for Pi
numberOfDigits = int(input("Please enter the number of decimal places to calculate Pi to: "))
getcontext().prec = numberOfDigits

# Chudnovsky Algorithm

# time execution of Pi
start_time = time.time()
# calc function
def calc(n):
    # declare variables
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    # forloop with variables
    for k in range(n):
        t = (Decimal(-1)**k)*(math.factorial(Decimal(6)*k))*(13591409+545140134*k)
        deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return str(pi)

# print results
print(calc(1))
print(Fore.BLUE + "\nTime of Calculation:", time.time() - start_time)
