#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with private size"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if (type(position) is tuple and position[0] is int and position[1] is int):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
