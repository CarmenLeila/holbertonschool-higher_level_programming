#!/usr/bin/python3

def uppercase(str):
    uppercase_chr = ''
    for i in str:
        if 97 <= ord(i) <= 122:
            uppercase_chr = chr(ord(i) - ord('a') + ord('A'))
        else:
            uppercase_chr = i
        print("{}".format(uppercase_chr), end="")
    print()

