#!/usr/bin/python3


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

    def __str__(self):
        """The __str__ magic method returns a
            String rep of the object
        """
        """Return:
            String: an empty string if the condition below is met"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""

        # for i in range(self.__height):
        #     [rect.append("#") for j in range(self.__width)]
        #     if i != self.__height - 1:
        #         rect.append("\n")
        # return ("".join(rect))
        """Return:
                List: A list containg the solution
        """
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    @property
    def width(self):
        """A getter for the width
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """A setter for the width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """A setter for height
        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """A getter for setting the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """A method for computing area"""
        """Area: L X W """
        """Return:
                int: area of the W and H using the
                    above formula
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """A method for computing the perimeter"""
        """Return:
            int: the perimeter of W and H or H and W
            """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            """Perimeter: 2(L+W)"""
            """Return:
                    int: Perimeter of H and W
            """
            perimeter = 2 * (self.__height + self.__width)
            return perimeter
