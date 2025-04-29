# guess1.py
# Lab 4.2.2 - programme to promt the user to guess a number

# Author: Lorraine Morrissey

# assign number
numbertoguess = 15

guess = int(input('Please guess the number: '))

while guess!= numbertoguess:
    print ('Wrong')
    guess = int(input('Please guess the again: '))
  
print ("Well done! The number was {}".format(numbertoguess))  