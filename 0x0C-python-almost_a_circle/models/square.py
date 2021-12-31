#!/usr/bin/python3

"""
Module square
Contains class Square, which inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """By inheriting the characteristics of Rectangle, defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes all attributes passed with their respective arguments"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get width of Rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """Set width to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
