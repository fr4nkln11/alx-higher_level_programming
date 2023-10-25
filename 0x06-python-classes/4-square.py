#!/usr/bin/python3
""" Access and update private attribute
This module defines a class Square
that defines a square by: (based on 3-square.py)
"""


class Square:
    """a class Square that defines a square by: (based on 3-square.py)
    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer,
            otherwise raise a TypeError exception
            with the message size must be an integer
            if size is less than 0,
            raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
        that returns the current square area
    """

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")

        self.__size = value

    def area(self):
        """calculate the area of a square

        Parameters:
            self: class instance

        Returns:
            area of the square
        """
        return self.__size**2
