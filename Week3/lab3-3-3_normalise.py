# normalise.py
# Lab 3.3.3 
#  a. read in string and removesleading or trailing spaces
#  b. convert the string to all lower case
#  c. oupt the length of the strings

# Author: Lorraine Morrissey

rawstring = input('Please enter a string: ')

#remove leading and trailin spaces using strip
normalisedstring = rawstring.strip()

# convert to lower
lowerstring = normalisedstring.lower()

# Length of strings
lenraw = len(rawstring)
lenformstring = len(normalisedstring)

# Print results
print('The string normalised is : {}'.format(normalisedstring))
print('The normalised string in all lower case is : {}'.format(lowerstring))
print('The string length decreased from {} to {}'.format(lenraw,lenformstring))