import functools
import time


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("Time: ", time.time() - start)
        return res
    return inner

@trace
def useful(x):
    print(2 ** x)


print(useful.__name__)
useful(1)
useful(10)
useful(100)
useful(100000)