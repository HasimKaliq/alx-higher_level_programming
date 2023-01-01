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
