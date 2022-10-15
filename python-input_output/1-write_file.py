#!/usr/bin/python3
"""module that contains the write_file function"""


def write_file(filename="", text=""):
    """writes text to filename and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as my_file:
        write_data = my_file.write(text)

    return write_data
