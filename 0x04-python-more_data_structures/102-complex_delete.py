#!/usr/bin/python3

def complex_delete(a_dictionary: dict, value):
    if a_dictionary:
        d_keys = []
        for k, v in a_dictionary.items():
            if v == value:
                d_keys.append(k)

        if d_keys:
            for key in d_keys:
                del a_dictionary[key]

    return a_dictionary
