#!/usr/bin/python3
from models.base import Base

"""Module rectangle
Contains class Rectangle, which inherits from Base
"""


class Rectangle(Base):
    """
    Inherits and extends from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all attributes passed with their respective arguments"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width to value"""
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Rectangle's height to value"""
        self.__height = value

    @property
    def x(self):
        """Get the x position of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x position of the Rectangle"""
        self.__x = value

    @property
    def y(self):
        """Get the x position of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the x position of the Rectangle"""
        self.__y = value
