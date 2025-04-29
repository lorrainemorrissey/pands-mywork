# topthree.py
# Lab 4.2.6 - programme to generate 10 random numbers, print them out and print out the top 3

# Author: Lorraine Morrissey

import random

howmany = 10
topthree = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in range(0,howmany):
    numbers.append(random.randint(rangefrom,rangeto))
print("{} random number\t {}".format(howmany,numbers))

topones = numbers.copy()

topones.sort(reverse = True)
print ("The top {} are \t\t {}".format(topthree,topones[0:topthree]))
