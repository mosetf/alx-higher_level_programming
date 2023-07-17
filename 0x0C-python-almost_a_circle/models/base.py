#!/usr/bin/python3
""" base module"""


class Base:
    """base of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id = None):
        """initialization
        Arg:
            id:has argument value
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
