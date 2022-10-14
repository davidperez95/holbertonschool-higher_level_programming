#!/usr/bin/python3
"""Module that defines the inherits_from function"""


def inherits_from(obj, a_class):
    """return True if obj is a subclass of a_class, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
