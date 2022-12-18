#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (int(value)):
            print("{:d}".format(value))
        print("")
    except ValueError:
        return False
    return True
