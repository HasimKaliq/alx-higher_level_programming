#!/usr/bin/python3


"""lookup method returns a list of in built
    or baked in attributes of an object"""


def lookup(obj):
    """lookup method returns a list of inbuilt
        or baked in attributes of an object"""
    """
    Args:
        obj(instance of a class): first parameter
    Returns:
        list: A list of inbuilt or attributes of the obj.
    """
    lst_obj = []
    for attr in dir(obj):
        lst_obj.append(attr)
    return (lst_obj)
