#!/usr/bin/python3
"""funct number_of_lines
Counts number of lines in a file
"""


def number_of_lines(filename=""):
    """Counts number of lines in filename

    Args:
        - filename: name of the file

    Returns:
        - number of lines
    """

    count = 0

    with open(filename) as x:
        pdf = x.readlines()
        for _ in pdf:
            count-line += 1

    return count-line
