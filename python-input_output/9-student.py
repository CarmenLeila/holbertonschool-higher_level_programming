#!/usr/bin/python3

"""
class that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        class that defines a student with first name , last name and age

        Args:
            first_name: first name
            last_name:  last name
            age:  age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method that retrieves a dictionary representation of a Student isntance
        """
        return self.__dict__
