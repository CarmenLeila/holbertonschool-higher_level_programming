#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for index in my_list:
            if index > max:
                max = index
        return max
    else:
        return None
