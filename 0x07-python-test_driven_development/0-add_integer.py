#!/usr/bin/python3
""" Integers addition
This module defines a function add_integer
"""

def add_integer(a, b=98):
    """ add two integers

    Params:
        @a: first integer
        @b: second integer

    Returns:
        sum of the two integers
    """
    if not (type(a) is int) and not (type(a) is float):
        raise TypeError("a must be an integer")

    if not (type(b) is int) and not (type(b) is float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
