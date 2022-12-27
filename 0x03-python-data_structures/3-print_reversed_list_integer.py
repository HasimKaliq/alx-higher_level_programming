#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 1:
        print("{:d}".format(my_list[0]))
    elif len(my_list) == 0:
        return None
    else:
        left = 0
        right = len(my_list) - 1
        while(left < right):
            temp = my_list[left]
            my_list[left] = my_list[right]
            my_list[right] = temp
            left += 1
            right -= 1
        for i in my_list:
            print("{:d}".format(i))

my_list = []
print_reversed_list_integer(my_list)