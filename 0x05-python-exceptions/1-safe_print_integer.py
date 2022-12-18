#!/usr/bin/python3
def safe_print_integer(value):
    try:
        convert = int(value)
        if (int(convert)):
            print("{:d}".format(convert))
            print("")
    except ValueError:
        return False
    return True