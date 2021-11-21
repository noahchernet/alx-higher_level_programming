#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list is None or my_list == []:
        print()
        return
    for i in my_list:
        print("{:d}".format(i))
