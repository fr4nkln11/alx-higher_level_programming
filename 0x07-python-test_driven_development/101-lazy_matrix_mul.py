#!/usr/bin/python3
import numpy as np
""" Lazy matrix multiplication
This module defines a function lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """ perform matrix multiplication with numpy

    Params:
        @m_a: matrix A
        @m_b: matrix B

    Returns:
        matrix product
    """
    A = np.array(m_a)
    B = np.array(m_b)

    return A.dot(B)
