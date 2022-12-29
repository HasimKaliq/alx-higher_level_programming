#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        max = my_list[0]
        for val_in_lst in my_list[1:]:
            if val_in_lst > max:
                max = val_in_lst
        return max
