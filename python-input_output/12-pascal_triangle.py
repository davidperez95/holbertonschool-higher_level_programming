#!/usr/bin/python3
"""This module contains the pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    if n <= 0:
        return []
    