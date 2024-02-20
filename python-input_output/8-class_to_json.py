#!/usr/bin/python3

"""
dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure

    Args:
        obj: instance of a class

    Returns:
        dictionary descritption
    """
    return obj.__dict__
