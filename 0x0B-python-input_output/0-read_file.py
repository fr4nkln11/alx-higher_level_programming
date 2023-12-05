#!/usr/bin/python3
"""
This module defines:

functions:
read_file
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    and prints it to stdout

    params:
    @filename: path to the file

    returns:
    Nothing
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
