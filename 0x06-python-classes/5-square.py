#!/usr/bin/python3
""" Printing a square
This module defines a class Square
that defines a square by: (based on 4-square.py)
"""


class Square:
    """ a class Square that defines a square by:
        Private instance attribute: size:
            property def size(self): to retrieve it
            property setter def size(self, value): to set it:
                size must be an integer,
                otherwise raise a TypeError exception
                with the message size must be an integer

                if size is less than 0,
                raise a ValueError exception
                with the message size must be >= 0
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method: def area(self):
            that returns the current square area
        Public instance method: def my_print(self):
            that prints in stdout the square with the character #:
                if size is equal to 0, print an empty line
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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculate the area of a square

        Parameters:
            self: class instance

        Returns:
            area of the square
        """
        return self.__size**2

    def my_print(self):
        """ prints in stdout the square with the character #

        Parameters:
            self: class instance

        Returns:
            nothing
        """

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
