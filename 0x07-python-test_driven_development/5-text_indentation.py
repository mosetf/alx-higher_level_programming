#!/usr/bin/python3
"""
funct text_indentation
Adds 2 new lines after a set of characters
"""


def text_indentation(text):
    """Prints text with added newlines
    when a ".", "?", ":" is encountered
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
