# outputstring.py
# Lab 3.3.2 Create and output simple string
# Author: Lorraine Morrissey

#Before format
message = 'John said hi I said bye'

# Use \t - tab break
message1 = 'John said\t"hi" I said\t "bye"'

# Use \n - new line
message2 = 'John said\t"hi" \n I said\t "bye"'

print ('Original string\n : {}'.format(message))
print ('Include tab breaks:\n {}'.format(message1))
print ('Include tab breaks and new line:\n {}'.format(message2))