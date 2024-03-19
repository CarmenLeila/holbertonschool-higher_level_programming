#!/usr/bin/python3
for len in range(0, 100):
    if len < 99:
        print("{:02d}, ".format(len), end='')
    else:
        print("{:02d}".format(len))