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
            """
            Raises:
                TypeError: If the argunment passed is not an int.
                ValueError: If the argunment passed is not >= 0.
            """
            if(type(self.__size) is not int):
                raise TypeError
            elif(type(self.__size) is int) and self.__size < 0:
                raise ValueError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
    def area(self):
        """The area fuction once the checks are valid
            Will return the square of self.__size.

        Returns:
            int: the square of the number self.__size.
        
        """ 
        return (self.__size * self.__size)
