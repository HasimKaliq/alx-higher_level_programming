#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """This a class, that has the private Variable size"""
    def __init__(self, size=0):
        """
        Args:
            size(int): The size for building the square
        """
        self.size = size

        if not isinstance(self.size, int):
            raise TypeError("size must be integer")
        elif self.size < 0:
            raise ValueError("must be >= 0")
        self.__size = size
    @property
    def size(self):
        """The size method returns the size
        Returns:
            int: the size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """The size method take an extra parameter,
            the value will be used to update self__size
        Args:
            value(int): the argument expected
        
        Raises:
            TypeError: If the argunment passed is not an int.
            ValueError: If the argunment passed is not >= 0.
            """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif(value < 0):
            raise ValueError("must be >= 0")
        self.__size = value

    def area(self):
        """The area fuction once the checks are valid
            Will return the square of self.__size.

        Returns:
            int: the square of the number self.__size.
        """
        return(self.__size * self.__size)
