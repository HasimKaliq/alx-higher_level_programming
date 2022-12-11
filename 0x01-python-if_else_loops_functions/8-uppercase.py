#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if(ord(i) in range(97, 123)):
            new_string +=  chr(ord(i) - 32)
        else:
            new_string += i
    print(new_string)
