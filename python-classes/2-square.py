#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square with private size"""
        if (type(size) is int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
