#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep = lambda element: element if (element != search) else replace
    new_list = list(map(rep, my_list))
    return new_list

