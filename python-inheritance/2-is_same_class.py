#!/usr/bin/python3

"""Defines if an object is an instance of the class"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
