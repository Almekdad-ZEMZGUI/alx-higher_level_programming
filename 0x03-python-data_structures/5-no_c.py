#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for char in my_string:
        if char != "C" and char != "c":
            res += char
    return res
