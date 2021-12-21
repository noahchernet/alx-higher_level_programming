#!/usr/bin/python3

"""3-to_json_string
Contains function to_json_string
"""


def to_json_string(my_obj):
    return __import__('json').dumps(my_obj)
