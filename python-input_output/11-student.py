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
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of a Student instance

        Args:
        attrs: attribute names to check if his contained in the list

        Returns:
            the dictionary or the new dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dictonary = {}

            for attribute in attrs:
                value = getattr(self, attribute, None)
                if value is not None:
                    new_dictonary[attribute] = value

            return new_dictonary
        
    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance

        Args:
            json: dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
