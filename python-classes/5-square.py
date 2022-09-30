#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square with private size"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self._size = size

    @property
    def size(self):
        """Getter method to return the size"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method to modify the size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self._size = value

    def area(self):
        """Returns the area of the square"""
        return (self._size * self._size)

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#")
