#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    
    index = 0
    try:
        for i in my_list:
            if index < x:
                print("{}".format(my_list[index]), end="")
                index += 1
        print()

    except IndexError:
        print("list out of index")

    return index
