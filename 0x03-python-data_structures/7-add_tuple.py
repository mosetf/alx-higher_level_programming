#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_tuple = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return n_tuple
