# Floor.py
# Lab 3.2.3 programme to take in float and output an int rounded down
# Author: Lorraine Morrissey

import math

numberfloat = float(input('Enter a float number: '))
floorednumber = math.floor(numberfloat)

print('{} floored is {}'.format(numberfloat, floorednumber))