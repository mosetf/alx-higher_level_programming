#!/usr/bin/python3
""" class Square """


class Square:
    """ this is the class i typed in line 2"""
    def __init__(self, size=0):
        if type(size) != int and type(size) != float:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        """🧐 if == other 🔲"""
        return(self.area() == other.area())

    def __lt__(self, other):
        """🧐 if < other 🔲"""
        return(self.area() < other.area())

    def __le__(self, other):
        """🧐 if <= other 🔲"""
        return(self.area() <= other.area())

    def __ne__(self, other):
        """🧐 if! = other 🔲"""
        return(self.area() != other.area())

    def __gt__(self, other):
        """🧐 if > other 🔲"""
        return(self.area() > other.area())

    def __ge__(self, other):
        """🧐 if >= other 🔲"""
        return(self.area() >= other.area())
