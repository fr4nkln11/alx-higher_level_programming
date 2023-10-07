#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    new_tup_a = []
    new_tup_b = []
    sum_a = 0
    sum_b = 0

    for i in range(2):
        if i < (a_len):
            new_tup_a.append(tuple_a[i])
        else:
            new_tup_a.append(0)

        if i < (b_len):
            new_tup_b.append(tuple_b[i])
        else:
            new_tup_b.append(0)

    sum_a = new_tup_a[0] + new_tup_b[0]
    sum_b = new_tup_a[1] + new_tup_b[1]

    return (sum_a, sum_b)
