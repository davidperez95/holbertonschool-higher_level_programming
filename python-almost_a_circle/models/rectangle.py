#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays to stdout the Rectangle with the # character"""
        for y in range(self.__y):
            print()

        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a grafic string of the Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args):
        """Updates the instance attributes"""
        for index, value in enumerate(args):
            if index == 0:
                self.id = value
            elif index == 1:
                self.__width = value
            elif index == 2:
                self.__height = value
            elif index == 3:
                self.__x = value
            elif index == 4:
                self.__y = value
