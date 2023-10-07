#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    sum_a = 0
    sum_b = 0

    if tuple_a and tuple_b:
        sum_a = tuple_a[0] + tuple_b[0]
        if a_len == b_len:
            sum_b = tuple_a[1] + tuple_b[1]
        else:
            sum_b = tuple_a[1] or tuple_b[1]
    else:
        sum_a = tuple_a[0] or tuple_b[0]
        sum_b = tuple_a[1] or tuple_b[1]


    return (sum_a, sum_b)
