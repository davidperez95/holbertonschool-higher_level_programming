#!/usr/bin/python3
"""This module contains the append_write function"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        write_data = my_file.write(text)
        return write_data
