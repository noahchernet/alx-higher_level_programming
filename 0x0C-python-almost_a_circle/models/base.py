#!/usr/bin/python3

"""Module base
Contains class Base
"""


class Base:
    """
    The base for all other classes in this project
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0  # Count the number of objects created from this class

    def __init__(self, id=None):
        """Class initializes here
        If id is None, it is set to __nb_objects after it's incremented
        """
        if id is not None:
            self.id = id
        else:
            #  __nb_objects is incremented only when id is None
            Base.__nb_objects += 1
            self.id = self.__nb_objects
