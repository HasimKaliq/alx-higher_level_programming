#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if(type(a and b) == int):
            result = a / b
        else:
            raise TypeError
    except(ZeroDivisionError, TypeError):
        result = None
        return None
    finally:
        if(result is None):
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {:.1f}".format(result))
    return result
