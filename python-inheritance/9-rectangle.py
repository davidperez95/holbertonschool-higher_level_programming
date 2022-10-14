#!/usr/bin/python3
"""Module that defines the Rectangle subclass"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Creates a new object Rectangle"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the Rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
