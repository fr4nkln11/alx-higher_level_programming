#!/usr/bin/python3
"""
This module defines:
functions:
    add_integer
"""


def add_integer(a, b=98):
    """
    a function that adds two integers

    params:
    a: first integer
    b: second integer

    returns:
    the addition of a and b
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if not type(a) is int:  # if `a` is not an integer
        raise TypeError("a must be an integer")
    elif not type(b) is int:  # if `b` is not an integer
        raise TypeError("b must be an integer")

    return a + b
