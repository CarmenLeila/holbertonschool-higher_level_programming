#!/usr/bin/python3

"""Class Rectangle"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """__init__ method
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: width of the rectangle
        setter method
        Args:
            width: width of the rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
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
        """height: height of the rectangle
        setter method
        Args:
            height: height of the rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area: returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__: string representation of the object"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for index1 in range(self.__height):
            for index2 in range(self.__width):
                string += "#"
            if index1 != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """__repr__: string representation of the object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    