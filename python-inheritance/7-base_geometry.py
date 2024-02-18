#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """class is empty"""
    pass

    def area(self):
        """instance method to calculate the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """instance method for verify if integer is valid"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
