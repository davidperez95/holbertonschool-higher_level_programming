#!/usr/bin/python3
"""Is same class modul"""


def is_same_class(obj, a_class):
    """
    Function that checks for if obj is instance of a_class
    Return True if obj is is instance
    False otherwise
    """
    return (type(obj) == a_class)
