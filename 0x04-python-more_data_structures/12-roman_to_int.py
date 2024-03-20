#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = dic[roman_string[-1]]
    for i in range(len(roman_string) - 1, 0, -1):
        if dic[roman_string[i - 1]] < dic[roman_string[i]]:
            res -= dic[roman_string[i - 1]]
        else:
            res += dic[roman_string[i - 1]]
    return res
