# iseven.py
# Lab 4.1.1 - programme to identify if number entered is even or odd

# Author: Lorraine Morrissey

# input number
number = int(input('Enter an integer: '))

# Use if to determine if even of odd
if (number%2) == 0:
    print ('{} is an even number'.format(number))

elif (number%2) != 0:
    print ('{} is an odd number'.format(number))