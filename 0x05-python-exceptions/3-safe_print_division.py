#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
        return result
    except(ZeroDivisionError, TypeError):
        return None
    finally:
        print("Inside result: {:.1f}".format(result))


a = "SA"
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))