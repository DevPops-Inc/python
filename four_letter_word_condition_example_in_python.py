#!/bin/python

# four letter word condition example in Python

word=input("Please enter a four-letter word: ")
word_length=len(word)
if word_length == 4:
    print(word, "is a four-letter world.  Well done.")
elif word_length == 3:
    print(word, "is a three-letter.  Try again")
else:
    print(word, "is not a four-letter word.")
