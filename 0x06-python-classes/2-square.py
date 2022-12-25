#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """This a class, that has the private Variable size"""
    def __init__(self, size=0):
        """
        Args:
            size(int): The size for building the square
        """
        self.__size = size
        try:
            if(type(self.__size) != int):
                raise TypeError("size must be an integer")
            elif(self.__size < 0):
                raise ValueError("size must be >= 0")
        except (ValueError, TypeError) as e:
            if(ValueError):
                print(e)
            if(TypeError):
                print(e)
