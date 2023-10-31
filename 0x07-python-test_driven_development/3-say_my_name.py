#!/usr/bin/python3
""" Say my name
This module defines a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """ print a string with the format
    My name is <first name> <last name>

    Params:
        @first_name: string
        @last_name: string

    Returns:
        None
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
