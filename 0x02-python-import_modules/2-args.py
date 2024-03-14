#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {:s}".format(i + 1, arg))
