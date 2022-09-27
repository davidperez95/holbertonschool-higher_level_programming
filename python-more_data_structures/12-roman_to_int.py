#!/usr/bin/python3


def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    number = 0

    for i in range(len(roman_string)):
        if (roman_string[i] in roman_dict):
            if (len(roman_string) != 1):
                number += roman_dict.get(roman_string[i])
            else:
                number += roman_dict.get(roman_string[i])

    return number
