#!/usr/bin/python3
""" 1-Square
This module defines
a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """ Square Class
    a class Square that defines a square by: (based on 0-square.py)
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        self.__size = size
