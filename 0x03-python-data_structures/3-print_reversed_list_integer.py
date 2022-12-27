#!/usr/bin/python3


"""If you're reading my code,
    I do apologize for my indulgence in details, that's who I am.
    If I can't build it from scratch, it's not fun,
    I always get a feeling of less fulfillment,
    when I have to call a method.
    Take the code below I could have called the method reverse on the list 
    but i'd loose the enjoyment
    of knowing how things work.
    maybe I give too much to details?
    or maybe it's bececause C made me do everything from scratch? either way,
    do enjoy!"""


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
