#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    printed = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
            printed += 1
            continue
        except (ValueError, TypeError):
            index += 1
            continue
    print()
    return printed
