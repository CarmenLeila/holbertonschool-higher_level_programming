#!/usr/bin/python3

"""Defines an object for lookup function"""


def lookup (obj):
    """
    Return the list of available attributes and methods of an object.
    
    Args:
        obj: The object to lookup

    Returns: 
        A list of available attributes and methods.
    """
    return dir(obj)
