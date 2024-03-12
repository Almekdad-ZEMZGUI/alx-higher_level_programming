#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            continue
        else:
            print(str[i], end="")
    print()
