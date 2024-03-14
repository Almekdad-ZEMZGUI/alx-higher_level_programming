#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    if len(argv) == 1:
        print(0)
    else:
        for arg in argv[1:]:
            result += int(arg)
        print(result)
