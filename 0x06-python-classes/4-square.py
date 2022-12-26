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
        try:
            """
            Raises:
                TypeError: If the argunment passed is not an int.
                ValueError: If the argunment passed is not >= 0.
            """
            if(type(self.size) is not int):
                raise TypeError
            elif(type(self.size) is int) and self.size < 0:
                raise ValueError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        else:
            self.__size = self.size

    def size(self):
        """The size method returns initaial size
        Returns:
            int: the initial passed value
        """
        try:
            """
            Raises:
                TypeError: If the argunment passed is not an int.
                ValueError: If the argunment passed is not >= 0.
            """
            if(type(self.size) is not int):
                raise TypeError
            elif(type(self.size) is int) and self.size < 0:
                raise ValueError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        else:
            return self.__size

    def size(self, value):
        """The size method take an extra parameter,
            the value will be used to update self__size
        Args:
            value(int): the argument expected
            """
        self.__size = value
        try:
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
        try:
            """
            Raises:
                TypeError: If the argunment passed is not an int.
                ValueError: If the argunment passed is not >= 0.
            """
            if(type(self.size) is not int):
                raise TypeError
            elif(type(self.size) is int) and self.size < 0:
                raise ValueError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        else:
            self.__size = self.size
            return(self.__size * self.__size)
