#!/usr/bin/python3
"""This module creates a class Square."""
class Square:
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """The setter function for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
