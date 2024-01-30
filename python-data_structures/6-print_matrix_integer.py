#!/usr/bin/python3
str = ""

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" ")
        print()