#!/usr/bin/python3
"""func append_after
inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts the new_string after
    the search_string in filename

    Args:
        - filename: file name
        - search_string: string to be updated
        - new_string: new_string to add onto
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
