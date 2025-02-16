# randomGenerator.py
# Lab 3.1 programme to print out random number between 1 and 10
# Author: Lorraine Morrissey

x = int(input("Enter the first number in the range: "))
y = int(input("Enter the end number of the range: "))

import random

number = random.randint (x,y)
print("Here is a random number {} between {} and {}".format(number, x, y))