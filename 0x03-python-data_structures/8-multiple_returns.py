#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is "" or sentence is None:
        return tuple((0, None))
    return tuple((len(sentence), sentence[0]))
