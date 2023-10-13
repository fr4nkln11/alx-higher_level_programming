#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        new_dict = {name: num * 2 for name, num in a_dictionary.items()}

    return new_dict
