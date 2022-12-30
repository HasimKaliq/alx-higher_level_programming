#!/usr/bin/python3


class Rectangle:

    # Public class attribute number_of_instances:
    # Initialized to 0
    # Incremented during each new instance instantiation
    # Decremented during each instance deletion
    number_of_instances = 0
    print_symbol = "#"

    def bigger_or_equal(rect_1, rect_2):
        """
        Static method def bigger_or_equal(rect_1, rect_2):
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

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        # The name of class is used to access the class
        # Attributes.
        Rectangle.number_of_instances += 1

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
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
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
        Rectangle.number_of_instances -= 1

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
