# numberqueue.py
# Lab 5.3 - programme to put 10 random numbers into a queue

# Author: Lorraine Morrissey

import random

queue = []
numberofnumbers = 10
rangeto = 100

##.append

for n in range(0,numberofnumbers):
    queue.append(random.randint(0,rangeto))

print("queue is{}".format(queue))

##.pop removes last item in the queue

while len(queue) !=0:
    currentnumber = queue.pop()
    print("current number is {} and the queue is {}".format(currentnumber,queue))

print("The queue is now empty")