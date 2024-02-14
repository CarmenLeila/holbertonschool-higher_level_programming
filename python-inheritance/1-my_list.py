#!/usr/bin/python3

"""class that inherits from list"""


class MyList(list):
    """class that prints the list, but sorted"""
    def print_sorted(self):
        """method for printing a sorted list"""
        print(sorted(self))
