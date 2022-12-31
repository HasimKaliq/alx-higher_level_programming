#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

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
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Static method
        that returns the biggest rectangle based on the area
        """
        """
        Args:
            rect_1(class A): The first parameter.
            rect_2(class A): The second parameter.

        Returns:
            instance: which of the instaces is large
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        elif isinstance(rect_1, Rectangle) and isinstance(rect_2, Rectangle):
            rect_area_1 = rect_1.area()
            rect_area_2 = rect_2.area()
            if rect_area_1 > rect_area_2:
                return rect_1
            elif rect_area_1 == rect_area_2:
                return rect_1
            else:
                return rect_2
