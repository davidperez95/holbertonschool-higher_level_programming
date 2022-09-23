#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()

    if idx < 0:
        return copy_list

    if idx > len(my_list):
        return copy_list

    for i in range(len(my_list)):
        if i == idx:
            copy_list[i] = element

    return copy_list
