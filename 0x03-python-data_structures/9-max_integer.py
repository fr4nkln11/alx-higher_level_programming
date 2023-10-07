#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for num in my_list:
            if num > max_int:
                max_int = num
    else:
        max_int = None

    return max_int
