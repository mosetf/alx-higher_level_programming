#!/usr/bin/python3
"""funct inherits_from
funct that return true if object is an instance of a clas that
inherited from specified class"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from a_class

    Args:
        - obj: object to be inspected
        - a_class: class to be checked

    Returns: True or False depending on the
    circumstances
    """

    return isinstance(obj, a_class) and type(obj) != a_class
