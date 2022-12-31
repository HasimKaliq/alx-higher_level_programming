#!/usr/bin/python3
"""a function that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    a_bunch_of_keys = a_dictionary.keys()
    if key in a_bunch_of_keys:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
