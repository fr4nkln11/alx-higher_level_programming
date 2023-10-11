#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = [list(map(lambda e: e ** 2 ,x)) for x in matrix]
        return new_matrix
    else:
        return []
