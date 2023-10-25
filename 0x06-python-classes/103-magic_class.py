#!/usr/bin/python3
""" Bytecode -> Python #5
This module defines a MagicClass
"""
import math


class MagicClass:
    """ a MagicClass defined by:
        Public instance method: def area(self)
        Public instance method: def circumference(self)

        Instantiation with radius:
            def __init__(self, radius):
    """
    def __init__(self, radius):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """ calculate the area
        with self.radius and PI
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ calculate the circumference
        with self.radius and PI
        """
        return (self.__radius * (2 * math.pi))
