#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string != str(roman_string) or roman_string is None:
        return None
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    nums = []

    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i] + roman_string[i + 1]\
                == "IX":
            nums.append(9)
            i += 2
            continue
        nums.append(int(symbols[roman_string[i].upper()]))
        i += 1
    return sum(nums)
