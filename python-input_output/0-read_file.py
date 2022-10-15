#!/usr/bin/python3
"""module that contains the read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
