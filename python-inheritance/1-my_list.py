#!/usr/bin/python3
"""Define My list class"""


class Mylist(list):
    """Subclass from list"""
    def __init__(self):
        """Create a new object or instance"""
        super().__init__()

    def print_sorted(self):
        """Print the list sorted"""
        print(sorted(self))
