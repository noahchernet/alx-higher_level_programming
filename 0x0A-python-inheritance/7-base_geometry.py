#!/usr/bin/python3

"""7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """
    Empty class with just one method
    """
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
        if type(value) is not int:
            raise TypeError(name.join(" must be an integer"))
        if value <= 0:
            raise ValueError(name.join(" must be greater than 0"))
