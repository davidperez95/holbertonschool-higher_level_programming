#!/usr/bin/python3


def add_integer(a, b=98):
    if (a is not int or a is not float):
        raise TypeError("a must be an integer")
    if (b is not int or b is not float):
        raise TypeError("a must be an integer")
    if (a is float):
        int(a)
    if (b is float):
        int(b)

    return (a + b)
