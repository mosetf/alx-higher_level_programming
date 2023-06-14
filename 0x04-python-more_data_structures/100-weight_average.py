#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    d = 0
    for tup_le in my_list:
        average += tup_le[0] * tup_le [1]
        d += tup_le[1]
    return float(average / d)
