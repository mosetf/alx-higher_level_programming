#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    v = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            v += 1
        except  Exception:
            x += 1
    print("")
    return v
