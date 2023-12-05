#!/usr/bin/python3
import json

"""
This module defines:

functions:
to_json_string
"""


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)

    params:
    @my_obj: object to serialize

    returns:
    serialize data in string
    """

    return json.dumps(my_obj)
