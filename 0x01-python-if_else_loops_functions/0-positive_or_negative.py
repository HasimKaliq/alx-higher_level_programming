#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("%d is positive" %number)
elif number == 0:
    print("%d is zero" %number)
elif number < 0:
    print("%d is negative" %number)
print('\n')
