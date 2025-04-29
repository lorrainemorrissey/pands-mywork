# guess2.py
# Lab 4.2.3 - programme to promt the user to guess a number

# Author: Lorraine Morrissey

# assign number
numbertoguess = 15

guess = int(input('Please guess the number: '))

while guess!= numbertoguess:
    if guess<numbertoguess:
        print ('too low')
    else:
        print  ('too high')
    guess = int(input('Please guess the again: '))
  
print ("Well done! The number was {}".format(numbertoguess))  