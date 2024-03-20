#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    tuple_sum = sum(list(map(lambda x: x[0] * x[1], my_list)))
    weight_sum = sum([ele[1] for ele in my_list])
    return tuple_sum / weight_sum
