#!/usr/bin/python3
""" Coordinates of a square
This module defines a class Square
that defines a square by: (based on 5-square.py)
"""


class Square:
    """a class Square that defines a square by:
    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer,
            otherwise raise a TypeError exception
            with the message size must be an integer

            if size is less than 0,
            raise a ValueError exception
            with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers,
            otherwise raise a TypeError exception
            with the message position must be
            a tuple of 2 positive integers
    Instantiation with optional size and optional position:
        def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
        that returns the current square area
    Public instance method: def my_print(self):
        that prints in stdout
        the square with the character #:

        if size is equal to 0, print an empty line
        position should be use by using space
        - Don’t fill lines by spaces when position[1] > 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if type(position) is tuple and len(position) == 2:
            for i in position:
                if i < 0 or not type(i) is int:
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            for i in value:
                if i < 0:
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """calculate the area of a square

        Parameters:
            self: class instance

        Returns:
            area of the square
        """
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #

        Parameters:
            self: class instance

        Returns:
            nothing
        """

        if self.__size == 0:
            print("")
        else:
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
