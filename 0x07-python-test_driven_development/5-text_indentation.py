#!/usr/bin/python3
""" Text indentation
This module defines a function text_indentation
"""


def text_indentation(text):
    if not type(text) is str:
        raise TypeError("text must be a string")

    indent_flag = False

    for char in text:
        if indent_flag:
            if char == " ":
                indent_flag = False
                continue
        print("{}".format(char), end="")
        if char in (".", "?", ":"):
            print("\n\n", end="")
            indent_flag = True
