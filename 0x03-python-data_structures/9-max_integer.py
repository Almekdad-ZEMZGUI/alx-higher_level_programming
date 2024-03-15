#!/usr/bin/python3
def max_integer(my_list=[]):
    max_list = 0
    if len(my_list) == 0:
        return None
    for ele in my_list:
        if ele > max_list:
            max_list = ele
    return max_list
