#!/usr/bin/python3
"""Module that defines the Rectangle subclass"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class that defines a Square"""
    def __init__(self, size):
        """Creates a new Square object"""
        self.__size = size

        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size * self.__size
