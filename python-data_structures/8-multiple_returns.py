#!/usr/bin/python3


def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len != 0:
        char = sentence[0]
    else:
        char = None

    new_tuple = (str_len, char)
    return new_tuple
