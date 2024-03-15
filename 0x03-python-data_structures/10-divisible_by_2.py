#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for ele in my_list:
        if ele % 2 == 0:
            res.append(True)
        else:
            res.append(False)
    return res
