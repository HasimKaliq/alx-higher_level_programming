#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        len_of_string = 0
        first_char_of_string = None
    else:
        len_of_string = len(sentence)
        first_char_of_string = sentence[0]
    return (len_of_string, first_char_of_string)
