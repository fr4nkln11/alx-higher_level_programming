#!/usr/bin/python3
""" Eval is magic
This module defines a class Rectangle
"""


class Rectangle:
    """ class Rectangle defines a rectangle by:
    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer,
            otherwise raise a TypeError exception
            with the message width must be an integer

            if width is less than 0,
            raise a ValueError exception
            with the message width must be >= 0

    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
        height must be an integer,
        otherwise raise a TypeError exception
        with the message height must be an integer

        if height is less than 0,
        raise a ValueError exception
        with the message height must be >= 0

    Instantiation with optional width and height:
        def __init__(self, width=0, height=0):

    Public instance method: def area(self):
        that returns the rectangle area
    Public instance method: def perimeter(self):
        that returns the rectangle perimeter:
        if width or height is equal to 0,
        perimeter is equal to 0

    print() and str() should print
    the rectangle with the character #:
        if width or height is equal to 0,
        return an empty string

    repr() should return a string representation
    of the rectangle to be able to recreate
    a new instance by using eval()
    """

    def __init__(self, width=0, height=0):
        self.__width = width

        if not (type(width) is int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height

        if not (type(height) is int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not (type(value) is int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not (type(value) is int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ calculate the area of a Rectangle
        Parameters:
            @self: current class instance

        Return:
            Area of Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ calculate the perimeter of a Rectangle
        Parameters:
            @self: current class instance

        Return:
            Perimeter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        output = []
        for i in range(self.__height):
            output.append("#" * self.__width)

        return "\n".join(output)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
