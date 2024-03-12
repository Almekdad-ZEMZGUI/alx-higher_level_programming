#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if 97 <= ord(w) <= 122:
            print("{}".format(chr(ord(w) - 32)), end="")
        else:
            print("{}".format(w), end="")
    print()
