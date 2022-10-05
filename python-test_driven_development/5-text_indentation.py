#!/usr/bin/python3
"""Module that brake a string after an expecific token"""


def text_indentation(text):
    """Function that prints a string with new lines after ., ?, and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    tokens = ['.', '?', ':']

    flag = 0

    for i in text:
        if flag == 0:
            if i == ' ':
                continue:
            else:
                flag = 1
        if flag == 1:
            if i in tokens:
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')
