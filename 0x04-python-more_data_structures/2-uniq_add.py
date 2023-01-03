#!/usr/bin/python3


"""a function that adds all unique integers in a list
    (only once for each integer)."""


def uniq_add(my_list=[]):
    """Addition of unique values in a list"""
    """Return:
        int: sum of unique elements
    """
    sum = 0
    uniq_ele = set(my_list)
    for val in uniq_ele:
        sum += val
    return sum
