# grade.py
# Lab 4.1.2 - programme to assign grade to inputted percentage mark

# Author: Lorraine Morrissey

# input mark
mark = int(input('Enter the percentage: '))

# Use if to determine the grade
if (mark < 0) or(mark>100):
    print ('Please enter a valid percentage between 0 and 100')

elif (mark<40):
    print ('{} is a Fail'.format(mark))

elif (mark>=40) and (mark<50):
    print ('{} is a Pass'.format(mark))

elif (mark>=50) and (mark<60):
    print ('{} is a Merit'.format(mark))

elif (mark>=60) and (mark<70):
    print ('{} is a Merit2'.format(mark))

else:
    print ('{} is a Distinction'.format(mark))
    