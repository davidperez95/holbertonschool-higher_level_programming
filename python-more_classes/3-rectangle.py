#!/usr/bin/python3
"""This module creates a Rectangle class"""


class Rectangle():
    """The rectangle class"""
    def __init__(self, width=0, height=0):
        """Constructor method for rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getther method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method fot the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method that return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns printable string reprentation of a rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return string
