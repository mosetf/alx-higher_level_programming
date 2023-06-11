#!/usr/bin/python3
def no_c(my_string):
    n_string =""
    for i in my_string:
        if i not in ('c', 'C'):
            n_string += i
    return n_string
