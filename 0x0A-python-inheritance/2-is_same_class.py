#!/usr/bin/python3

def is_same_class(obj, a_class):
    """a function that check of instace
    Args:
        obj(instance) - Parameter 1
        a_class(class) - Parameter 2
    Return:
        Bool: True if  instance
              False if not
    """
    try:
        if obj.__class__ is a_class:
            return True
        else:
            return False
    except ValueError:
        return None
