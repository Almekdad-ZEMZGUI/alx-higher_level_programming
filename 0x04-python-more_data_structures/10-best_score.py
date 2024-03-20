#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        _max = max([v for v in a_dictionary.values()])
        for k, v in a_dictionary.items():
            if v == _max:
                return k
    return None
