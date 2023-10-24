#!/usr/bin/python3
"""funct 2-append_write
Appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """Appends text to filename

    Args:
        - filename:file name
        - text: text to be appended
    Returns: number of characters appended
    """

    with open(filename, 'a+') as x:
        return x.write(text)
