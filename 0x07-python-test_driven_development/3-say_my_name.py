#!/usr/bin/python3
""" Say my name
This module defines a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
