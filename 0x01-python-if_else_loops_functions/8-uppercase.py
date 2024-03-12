#!/usr/bin/python3
def uppercase(str):
    for i, w in enumerate(str):
        if 97 <= ord(w) <= 122:
            w = chr(ord(w) - 32)
            print("{}".format(w), end="\n" if i == len(str) - 1 else "")
        else:
            print("{}".format(w), end="" if i == len(str) - 1 else "")
