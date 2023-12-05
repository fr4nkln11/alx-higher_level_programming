#!/usr/bin/python3
"""
This module defines:

functions:
append_write
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    params:
    @filename: path to the file
    @text: text to write in the file

    returns:
    the number of characters added
    """

    length = None
    with open(filename, "a", encoding="utf-8") as file:
        length = file.write(text)

    return length
