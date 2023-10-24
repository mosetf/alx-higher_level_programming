#!/usr/bin/python3
"""funct is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """funct that checks if an object is an instance of a class
    Args:
        obj:object to be analyzed
        a_class: the class that instantiates an object
    Return:True if object is an instance of a class
    else False
    """
    return isinstance(obj, a_class)
