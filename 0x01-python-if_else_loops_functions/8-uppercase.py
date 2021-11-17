#!/usr/bin/python3


def uppercase(str):
    n = ''
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            if i == len(str) - 1:
                n = '\n'
            print("{}{}".format(chr(ord(str[i]) - 32), n), end="")
        else:
            if i == len(str) - 1:
                n = '\n'
            print("{}{}".format(str[i], n), end="")
