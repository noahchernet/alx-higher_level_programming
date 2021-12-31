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

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
