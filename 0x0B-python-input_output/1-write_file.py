#!/usr/bin/python3
"""
This module defines:

function:
write_file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written

    params:
    @filename: path to the file
    @text: text to write in the file

    returns:
    the number of characters written
    """

    length = None

    with open(filename, "w", encoding="utf-8") as file:
        length = file.write(text)

    return length
