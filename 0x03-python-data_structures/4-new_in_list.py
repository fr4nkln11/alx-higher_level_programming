#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = [el for el in my_list]
    if idx > 0 and idx < len(my_list):
        list_copy[idx] = element
    return list_copy
