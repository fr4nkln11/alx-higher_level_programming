#!/usr/bin/python3
def weight_average(my_list=[]):
    w_avg = 0
    if my_list:
        product_sum = sum(x[0] * x[1] for x in my_list)
        weight_sum = sum(x[1] for x in my_list)

        return product_sum / weight_sum

    return w_avg
