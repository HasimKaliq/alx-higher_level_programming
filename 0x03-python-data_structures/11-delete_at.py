#!/usr/bin/python3

"""This is the most basic pop() from the ground up,
    at least my own implementation 😂😂"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
