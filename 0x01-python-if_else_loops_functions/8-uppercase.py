#!/usr/bin/python3


def uppercase(str):
    n = ''
    to_print = ""
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            to_print += chr(ord(str[i]) - 32)
        else:
            to_print += str[i] + n
    print(to_print)
