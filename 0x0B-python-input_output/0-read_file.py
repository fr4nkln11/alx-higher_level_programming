#!/usr/bin/python3
"""
This module defines:

functions:
read_file
"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
