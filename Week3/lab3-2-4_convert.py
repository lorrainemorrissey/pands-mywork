# convert.py
# Lab 3.2.4 - take in a float amount of dollars and returns the absolute amount in cent
# Author: Lorraine Morrissey

# Layer int, round and absolute to ensure positive integer returned

amount = float(input('Enter a $ amount: '))
cent = int(round(abs((amount*100))))


print('${} in cent is {}'.format(amount, cent))