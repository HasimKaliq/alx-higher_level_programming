#!/usr/bin/python3
def islower(c):
    is_lower_upper = ord(c)
    if (is_lower_upper in range(97, 123)):
        return True
    elif (is_lower_upper in range(65, 91)):
        return False
