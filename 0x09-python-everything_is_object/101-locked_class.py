#!/usr/bin/python3
""" Low memory cost
This module defines a class LockedClass
"""


class LockedClass(object):
    """ a class LockedClass
    with no class or object attribute,
    that prevents the user from
    dynamically creating new
    instance attributes, except if
    the new instance attribute is called
    first_name.
    """

    __slots__ = ['first_name']
