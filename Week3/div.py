# div.py
# Lab 3.1 programme to readin two number and divide the first by the second and give integer result and remainder
# Author: Lorraine Morrissey

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x/y)
remainder = x%y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))