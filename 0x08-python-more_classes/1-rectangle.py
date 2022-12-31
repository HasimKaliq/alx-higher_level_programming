#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Constructs a Rectangle object"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        """
    Args:
        width(int): the first parameter
        height(int): the second parameter
    """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """A Getter method
        Return:
            int: The retrieved width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """The setter method for the width
        Args:
            width(int): a single width parameter
        Return:
            int: the width is returned
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """A Getter method for retrieving height
        Return:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """The method for setting the height
        Args:
            height(int): a single height parameter
        Return:
            The height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
