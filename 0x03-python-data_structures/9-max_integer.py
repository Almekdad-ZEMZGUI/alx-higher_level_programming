#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_list = my_list[0]
    for ele in my_list:
        if ele > max_list:
            max_list = ele
    return max_list
