# guess2.py
# Lab 4.2.4 - programme to promt the user to guess a number (using random generator to select number)

# Author: Lorraine Morrissey

# assign randomnumber

import random

numbertoguess = random.randint(0,100)

guess = int(input('Please guess the number: '))

while guess!= numbertoguess:
    if guess<numbertoguess:
        print ('too low')
    else:
        print  ('too high')
    guess = int(input('Please guess the again: '))
  
print ("Well done! The number was {}".format(numbertoguess))  