#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))

#    for row in matrix:
#        for item in row:
#            if item == row[-1]:
#                print("{:d}".format(item))
#            else:
#                print("{:d}".format(item), end=' ')
