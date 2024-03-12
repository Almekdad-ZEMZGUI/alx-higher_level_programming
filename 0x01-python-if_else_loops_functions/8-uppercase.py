#!/usr/bin/python3
def uppercase(str):
    for i, w in enumerate(str):
        if 97 <= ord(w) <= 122:
            w = chr(ord(w) - 32)
        print("{}".format(w), end="")
    print()
