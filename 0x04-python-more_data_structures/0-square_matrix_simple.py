#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for vec in matrix:
            n_vec = [el for el in vec]
            new_matrix.append(list(map(lambda e: e ** 2, n_vec)))

    return new_matrix
