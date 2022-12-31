#!/usr/bin/python3

"""a function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    a_bunch_of_keys = list(a_dictionary.keys())
    a_bunch_of_keys.sort()
    for keys in a_bunch_of_keys:
        print("{}: {}".format(keys, a_dictionary[keys]))
