#!/usr/bin/python3

"""7-base_geometry
Contains class BaseGeometry
"""

__import__('sys').path.insert(1, '../')
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Empty class with just one method
    """
    def __init__(self, width, height):
        """Initialize the object's values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Function is not implemented yet, so it raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises appropriate exceptions with messages. Doesn't do anything
        in particular
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
