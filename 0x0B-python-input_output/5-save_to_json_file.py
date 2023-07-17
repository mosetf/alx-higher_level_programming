#!/usr/bin/python3
"""funct save_to_json_file
Writes an object to a text file using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj to filename

    Args:
        - my_obj: object tobe written
        - filename: file to write to
    """

    with open(filename, 'w+') as x:
        json.dump(my_obj, x)
