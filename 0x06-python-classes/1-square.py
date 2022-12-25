#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """This a class, that has the private Variable size"""
    def __init__(self, size):
        """
        Args:
            size(int): The size for building the square
        """
        self.__size = size
