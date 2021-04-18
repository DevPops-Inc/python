#!/bin/python

# four letter word condition example in Python

# prompt user input
str(input("\nDetermine if a string is a four letter word.\nPress any key to continue or press Ctrl and C keys to quit."))

# declare word and worldLength varibles
word=str(input("\nPlease enter a four-letter word: \n"))
wordLength=len(word)

# if statements to determine four letter word condition
if wordLength == 4:
    print(word, "is a four-letter world.  Well done.\n")
elif wordLength == 3:
    print(word, "is a three-letter.  Try again\n")
else:
    print(word, "is not a four-letter word.\n")
