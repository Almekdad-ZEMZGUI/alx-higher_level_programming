#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for ele in my_list[:x]:
            print("{:d}".format(ele), end="")
            count += 1
        print()
        return count
    except (IndexError, TypeError):
        print()
        return count
