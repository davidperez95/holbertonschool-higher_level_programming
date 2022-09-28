#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError as error:
        result = None
        sys.stderr.write("Exception: " + str(error) + "\n")
    except IndexError as error:
        result = None
        sys.stderr.write("Exception: " + str(error) + "\n")

    return result
