#!/usr/bin/python3
"""
This module defines:

function:
lookup
"""


def lookup(obj):
    """
    a function that returns the list
    of available attributes and methods of an object

    params:
    @obj: a python object

    returns:
    a list containing attributes and methods
    """

    return dir(obj)
