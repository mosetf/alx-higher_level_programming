#!/usr/bin/python3
def multiple_returns(sentence):
    nt = ()
    if len(sentence) == 0:
        nt = 0, "None"
    else:
        nt = (len(sentence), sentence[0])
        return nt
