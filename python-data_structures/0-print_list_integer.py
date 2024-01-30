#!/usr/bin/python3
"""Prints all integers of a list."""

str = ''

def print_list_integer(my_list=[]):
    for index in my_list:
        print("{:d}".format(index))