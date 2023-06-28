#!/usr/bin/python3
"""magic class """
import math


class MagicClass:
    """ it works the same way as asked by the task 👨‍🦯👨‍🦯👨‍🦯"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ calcs area 😂"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """performs some math and comes up with the earths circumference 😂😂💔"""
        return (2 * math.pi) * self.__radius
