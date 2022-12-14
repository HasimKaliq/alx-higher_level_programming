#!/usr/bin/python3
"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    elif isinstance(a_dictionary, dict):
        dict_by_values = list(a_dictionary.values())
        dict_by_values.sort()
        largest_val = dict_by_values[len(dict_by_values)-1]
        for key in a_dictionary.keys():
            if a_dictionary[key] == largest_val:
                return key
    else:
        return None
