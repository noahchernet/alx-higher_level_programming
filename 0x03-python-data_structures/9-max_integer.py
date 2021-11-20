#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_num = 0
    for i in my_list:
        if max_num < i:
            max_num = i

    return max_num
