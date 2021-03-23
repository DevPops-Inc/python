#!/bin/python

# count heads or tails in coin flips

# import random module
import random

str(input("\nLet's count heads or tails in coin flips!\nPress any key to continue.\n"))

# declare variables
output={"Heads":0, "Tails":0}
coin=list(output.keys())
coinFlip=int(input("Type the number of coin flips you want: \n"))

# for loop in range
for i in range(coinFlip):
    output[random.choice(coin)]+=1

# print results
print("\nThe results of the coin flips are: \n")
print("Heads:", output["Heads"])
print("Tails:", output["Tails"])
