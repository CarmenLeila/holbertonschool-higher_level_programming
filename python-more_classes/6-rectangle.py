#!/usr/bin/python3

"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method to return the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of the width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to return the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of the height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method for getting  the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Method for getting the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that returns the string representation of the rectangle"""
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
        """Method that returns the string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes an instance of Rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
