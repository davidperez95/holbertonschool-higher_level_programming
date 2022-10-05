#!/usr/bin/python3
"""Module that divides a all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that checks matrix and pass div to the sublist"""

    type_error_str = "matrix must be a matrix (list of lists)\
        of integers/floats"

    """Verify div type"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    """Verify div value"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Verify if matrix is a list"""
    if type(matrix) is not list:
        raise TypeError(type_error_str)

    """Verify if matrix contain only lists"""
    for i in matrix:
        if type(i) is not list:
            raise TypeError(type_error_str)

    """Verify if the lists in matrix have the same length"""
    lists_length = len(matrix[0])
    for i in matrix:
        if len(i) != lists_length:
            raise TypeError("Each row of the matrix must have the same size")

    """Verify if the lists in matrix contain only ints or floats"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and \
                    type(matrix[i][j]) is not float:
                raise TypeError(type_error_str)

    """Execute the division"""
    new_matrix = list(map(list, matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
