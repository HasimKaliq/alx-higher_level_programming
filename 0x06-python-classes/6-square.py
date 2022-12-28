#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """This a class, that has the private Variable size"""
    def __init__(self, size=0, position = (0, 0)):
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
        if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, x, y):
        self.__position[0] = x
        self.__position[1] = y

    def area(self):
        """The area fuction once the checks are valid
            Will return the square of self.__size.

        Returns:
            int: the square of the number self.__size.
        """
        return(self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            for i in range(1, self.__size + 1):
                print("#", end="")
            print()

Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
print(my_square_3.position)
print("--")