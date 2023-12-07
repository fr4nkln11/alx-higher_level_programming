#!/usr/bin/python3
"""
This module defines:

class:
MyList
"""


class MyList(list):
    """
    a class MyList that inherits from list
    Public instance method:
        def print_sorted(self):
            prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        print(sorted(self))
