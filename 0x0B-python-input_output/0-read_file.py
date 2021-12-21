#!/usr/bin/python3

"""0-read_file
Contains function read_file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to the standard output

    Args:
        filename (str): name of the file to open and read
    """
    with open(filename, "r") as f:
        print(f.read())
