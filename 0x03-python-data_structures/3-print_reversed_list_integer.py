#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i), end="\n")
    return None
