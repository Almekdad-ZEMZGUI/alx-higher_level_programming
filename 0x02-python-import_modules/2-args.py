#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments.".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {}".format(i, arg))
