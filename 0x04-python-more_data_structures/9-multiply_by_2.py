#!/usr/bin/python3
"""a function that returns a new dictionary
    with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    squared_dict = {}
    for key, values in a_dictionary.items():
        squared_dict[key] = values * 2
    return squared_dict
