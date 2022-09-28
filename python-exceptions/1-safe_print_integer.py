#!/usr/bin/python3


def safe_print_integer(value):

    check_value = isinstance(value, int)
    
    try:
        if (check_value is True):
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
