#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as error:
        sys.stderr.write("Exception: " + str(error) + "\n")
        return False
    except TypeError as error:
        sys.stderr.write("Exception: " + str(error) + "\n")
        return False
