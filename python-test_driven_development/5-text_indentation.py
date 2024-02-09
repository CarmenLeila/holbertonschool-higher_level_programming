#!/usr/bin/python3
"""
brand new module
"""


def text_indentation(text):
    """
    This is a function
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for ch in text:
        result += ch
        if ch in ('?', '.', ':'):
            result += '\n\n'
    results = result.split('\n')

    for index in range(len(results)):
        if index != (len(results) - 1):
            print(results[index].strip())
        else:
            print(results[index].strip(), end="")
