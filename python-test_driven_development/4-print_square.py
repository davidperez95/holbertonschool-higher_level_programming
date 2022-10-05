#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """This function prints a square based no size"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
