#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep(element):
        if element == search:
            return replace
        else:
            return element

    new_list = list(map(rep, my_list))
    return new_list
