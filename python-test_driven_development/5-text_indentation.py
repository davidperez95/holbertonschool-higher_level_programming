#!/usr/bin/python3
"""Module that brake a string after an expecific token"""


def text_indentation(text):
    """Function that prints a string with new lines after ., ?, and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    tokens = ['.', '?', ':']

    for char in range(len(text)):
        if text[char] in tokens:
            print("{}".format(text[char]))
            print("")
        elif text[char] == ' ' and text[char - 1] in tokens:
            continue
        else:
            print("{}".format(text[char]), end='')
