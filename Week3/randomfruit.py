# randomfruit.py
# Lab 3.1 programme to print out random fruit
# Author: Lorraine Morrissey

import random

fruits = ["apple", "Orange", "Banana", "Pear", "Grape", "Fig"]
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A random Fruit: {}".format(fruit))