#!/usr/bin/python3
""" Divide a matrix
This module defines a function matrix_divided
"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix.

    Params:
        @matrix: a list of lists containing integers or floats
        @div: an integer or float that divides
            each element of the matrix

    Returns:
        a new matrix containing the divided numbers
    """
    row_count = None
    new_matrix = []
    type_error = TypeError(
        "matrix must be a matrix (list of lists) of integers/floats")
    if not type(matrix) is list:
        raise type_error

    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not type(row) is list:
            raise type_error

        if not row_count:
            row_count = len(row)
        else:
            if len(row) != row_count:
                raise TypeError(
                    "Each row of the matrix must have the same size")

        for index in range(row_count):
            if not type(row[index]) is int and not type(row[index]) is float:
                raise type_error
            quotient = row[index] / div
            new_row.append(round(quotient, 2))

        new_matrix.append(new_row)

    return new_matrix
