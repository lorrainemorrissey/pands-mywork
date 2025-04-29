# nameAndage.py
# This programme asks user yo input their name and age
# Author: Lorraine Morrissey

name = input("What is your name?")
age = int(input("What age are you?"))
newage = age + 1

print ("Hello " + name +" you are " f'{age}' + " years old")
print (name +"\t on your next birthday" + " you will be " + f'{newage}' + " years old")