#!/usr/bin/python3
"""funct is_same_class"""


def is_same_class(obj, a_class):
    """funct to determine if obj is an instance of a class

    Args:
        - obj: object to look at
        - a_class: class to verify its instance

    Returns: True if obj is an instance of a class
    else false
    """
    if type(obj) is a_class:
        return True
    return False
