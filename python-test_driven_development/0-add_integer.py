#!/usr/bin/python3
"""Module that adds to integers"""


def add_integer(a, b=98):
    """function that add two integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if (a is float):
        int(a)
    if (b is float):
        int(b)

    return (a + b)
