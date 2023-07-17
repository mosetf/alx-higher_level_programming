#!/usr/bin/python3
""" module rectangle """
from base import Base


class Rectangle(Base):
    """
    initializes a rectangle
    arg:
        width: rectangles width
        height:rectangles height
        x: x
        y:y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initilize"""
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
