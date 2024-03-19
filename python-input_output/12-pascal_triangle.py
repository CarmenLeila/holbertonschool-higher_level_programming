#!/usr/bin/python3

"""
module for the triangle of Pascal
"""


def pascal_triangle(n):
    """function that creates the triangle of Pascal

    Args:
        n: size of the Pascal triangle

    Returns:
        a list of lists of integers representing the Pascal’s triangle
    """
    if n < 1:
        return []

    triangle = []
    first_line = [1]

    triangle.append(first_line)

    for line in range(1, n):
        new_line = [1]
        for column in range(1, len(first_line)):
            new_line.append(first_line[column - 1] + first_line[column])

        new_line.append(1)
        first_line = new_line
        triangle.append(new_line)

    return triangle
