#!/usr/bin/python3


def multiple_returns(sentence):
    length, first = len(sentence), sentence[0]
    if length == 0:
        return (length, None)
    return (length, first)
