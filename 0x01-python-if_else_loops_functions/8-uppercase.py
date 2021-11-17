#!/usr/bin/python3


def uppercase(str):
    if str == "":
        print("")
        return

    for i in range(0, len(str)):
        # c is the character to be printed
        c = chr(ord(str[i]) - 32) if 97 <= ord(str[i]) <= 122 else str[i]
        newline_placeholder = '\n' if i == len(str) - 1 else ''
        print("{}{}".format(c, newline_placeholder), end="")
