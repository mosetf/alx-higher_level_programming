#!/usr/bin/python3
"""func read_file
Reads from a file and prints
"""


def read_file(filename=""):
    """Reads filename contents anf prints them

    Args:
        filename: name of the file
    """

    with open(filename) as x:
        read_text = x.read()
        print(read_text, end="")
