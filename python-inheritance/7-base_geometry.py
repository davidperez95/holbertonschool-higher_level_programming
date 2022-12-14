#!/usr/bin/python3
"""Module that defines the BaseGeometry Class"""


class BaseGeometry():
    """super class BaseGeometry"""
    def __init__(self):
        """pass on create a new instance"""
        pass

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
