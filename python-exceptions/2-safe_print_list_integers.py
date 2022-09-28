#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    index = 0
    for i in range(x):
        try:
            if (type(my_list[i]) is int and index != x):
                print("{:d}".format(my_list[i]), end="")
                index += 1
        except IndexError:
            print("list index out of range")

    print()
    return index
