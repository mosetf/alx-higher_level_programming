#!/usr/bin/python3
"""func load_from_json_file
Creates an object from JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an object from filename

    Args:
        -    filename: name of the file
    Returns: object
    """

    with open(filename, 'r') as x:
        return json.load(x)
