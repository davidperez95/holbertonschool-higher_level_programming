#!/usr/bin/python3
"""The base module"""


class Base():
    """Base class with:
    __nb_objects as a class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Object constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
