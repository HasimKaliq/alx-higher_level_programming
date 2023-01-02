#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""

        # for i in range(self.__height):
        #     [rect.append("#") for j in range(self.__width)]
        #     if i != self.__height - 1:
        #         rect.append("\n")
        # return ("".join(rect))

        for i in range(self.__height):
            for i in range(self.__width):
                rect.append("#")
            if i == self.__width-1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Expected output:--> Rectangle(width, height)"""
        """I could using string write the name of the class"""
        """like so "Rectangle, but if we change the class name"""
        """it become less flexible and breaks, sooooo"""
        """The solution below save the name of the class using"""
        """self.__class__ since self is the instance of the class"""
        """Then use the varibale name.__name__ to get the origin"""
        """The actual name of the class, you know the one with the"""
        """Capital letter starting it.😁"""
        name_of_class = self.__class__
        return f"{name_of_class.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """Area: L X W """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            """Perimeter: 2(L+W)"""
            perimeter = 2 * (self.__height + self.__width)
            return perimeter
