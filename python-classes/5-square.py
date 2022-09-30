#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square with private size"""
        self.size = size

    @property
    def size(self):
        """Getter method to return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to modify the size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
