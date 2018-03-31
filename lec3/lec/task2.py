import functools
import time


def trace(func):
    """ Decorator, counts work-time of given function and returns it."""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("Time: ", time.time() - start)
        return res
    return inner

@trace
def useful(x):
    """ Prints 2 in power of given number."""
    print(2 ** x)


print(useful.__name__)
useful(1)
useful(10)
useful(100)
useful(100000)