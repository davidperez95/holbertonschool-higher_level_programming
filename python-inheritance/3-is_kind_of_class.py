#!/usr/bin/python3
"""Module that checks for an instance"""


def is_kind_of_class(obj, a_class):
    """
    Return true if obj is instance of a a_class
    or a subclass of a_class
    """
    return (isinstance(obj, a_class))
