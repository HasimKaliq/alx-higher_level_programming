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
    return (dir(object))
