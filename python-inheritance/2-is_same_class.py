#!/usr/bin/python3

"""Defines if an object is an instance of the class"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of the specified class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is exactly an instance of a_class, otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
