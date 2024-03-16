#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("{}".format(""))
        else:
            for ele in row:
                print("{:d}".format(ele), end=" " if ele != row[-1] else "\n")
