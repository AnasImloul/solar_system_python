from random import random


def multiply(iterable, value):
    return tuple(k * value for k in iterable)


def randbetween(start, end):
    return start + (end  - start) * random()


def inverse(color):
    return tuple(255 - c for c in color)