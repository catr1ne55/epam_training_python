import functools
import time


def trace(func):
    """ Decorator which counts work-time of given function and returns it.

    :param func: Function to handle.
    :type func: function
    :returns inner: Function that returns working time of func.
    :rtype function
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("Time: ", time.time() - start)
        return res

    return inner


@trace
def useful(x):
    """ Prints 2 in power of given number.

    :param x: Number
    :type x: int
    """
    print(2 ** x)


print(useful.__name__)
useful(1)
useful(10)
useful(100)
useful(100000)
