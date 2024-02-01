#!/usr/bin/python3


def best_score(a_dictionary):
    max_score = 0
    max_key = ''
    if a_dictionary is None or len(a_dictionary.values()) == 0:
        return None
    for item in a_dictionary.items():
        if item[1] > max_score:
            max_score = item[1]
            max_key = item[0]
    return max_key
