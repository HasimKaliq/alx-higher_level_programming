#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = f"{number}"
last_index_val = int(num_str[len(num_str)-1])
if (last_index_val > 5):
    print(f"Last digit of {number} is {last_index_val} and is greater than 5")
elif (last_index_val == 0):
    print(f"Last digit of {number} is {last_index_val} and is 0")
elif (last_index_val < 6):
    print(f"Last digit of {number} is {last_index_val} and is less than 6 and not 0")

