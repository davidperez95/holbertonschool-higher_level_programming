#!/usr/bin/python3
"""Define My list class"""


class Mylist(list):
    """subclass from list"""
    def __init__(self):
        """create a new object or instance"""
        super().__init__()

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
