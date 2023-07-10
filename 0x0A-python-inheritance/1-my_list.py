#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList (list):
    """class mylist"""
    def print_sorted(self):
        """module that prints a list sorted in a ascending order"""
        sort_ted = sorted(self)
        for i in sort_ted:
            print("{}".format(i))
