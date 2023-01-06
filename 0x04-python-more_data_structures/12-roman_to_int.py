#!/usr/bin/python3
""" Technical interview preparation:
    - You are not allowed to google anything
    - Whiteboard first
    - Create a function def roman_to_int(roman_string):
        - that converts a Roman numeral to an integer.
        - You can assume the number will be between 1 to 3999.
        - def roman_to_int(roman_string) must return an integer
        - If the roman_string is not a string or None, return 0"""
"""
--------------------------------------
| I | V |  X |  L |   C |   D |  M   |
| 1 | 5 | 10 | 50 | 100 | 500 | 1000 |
--------------------------------------
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum_of_roman_to_int = 0
    roman_to_int = []
    modern_base_numeral = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(len(roman_string)):
        roman_to_int.append(modern_base_numeral[roman_string[i]])
    print(roman_to_int)
    for i in range(0, len(roman_to_int)-1):
        print(type(roman_to_int[i]))
        if roman_to_int[i] < roman_to_int[i+1]:
            sum_of_roman_to_int += roman_to_int[i+1] - roman_to_int[i]
        elif roman_to_int[i] >= roman_to_int[i+1]:
            sum_of_roman_to_int += roman_to_int[i]
    print(sum_of_roman_to_int)

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))