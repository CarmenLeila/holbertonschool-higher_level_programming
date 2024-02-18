#!/usr/bin/python3
"""defines a class that inherits"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        """instance method to  calculate the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """instance method to verify if integer is valid"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherited class for making a rectangle"""
    def __init__(self, width, height):
        """ define instance of a rectange with his width and height

        Args:
            width: private attribute width
            height: private attribute height
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

        def area(self):
            return self.__width * self.__height
        
        def __str__(self):
            return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
