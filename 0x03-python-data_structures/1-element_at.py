#!/usr/bin/python3
def element_at(my_list, idx):
    list_length = len(my_list)
    if idx < 0:
        return None
    elif idx >= list_length:
        return None
    else:
        return my_list[idx]
