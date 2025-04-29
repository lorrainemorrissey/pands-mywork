# average.py
# Lab 4.2.5 - programme to calculate the average of the numbers input (stop input when user enters 0)

# Author: Lorraine Morrissey

numbers[]

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter number (0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print("The aveerage is{}".f(average))