import math
from functools import cache


def memoize(function):
    cache = dict()

def memoized_function(*args):
    if args in cache:
        return cache[args]
    result =  function(*args)
    cache[args] = result
    return result
    return memoized_function
print(memoized_function)