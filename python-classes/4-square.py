#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square with private size"""
        if (type(size) is int):
            self._Square__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        """Getter method to return the square value"""
        return self._Square__size

    def size(self, value):
        """Setter method to change the square value"""
        self._Square__size = value

    def area(self):
        """Returns the area of the square"""
        return (self._Square__size * self._Square__size)
