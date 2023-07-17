#!/usr/bin/python3
""" module rectangle """
from models.base import Base


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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
