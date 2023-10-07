#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        inner_length = len(matrix[0])
        for inner in matrix:
            for i in range(inner_length):
                if i < inner_length - 1:
                    print("{:d} ".format(inner[i]), end="")
                else:
                    print("{:d}".format(inner[i]))

