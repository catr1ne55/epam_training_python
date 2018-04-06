import functools
import operator


def factorial(n):
    """ Compute the factorial of given number.

    :param n: Number.
    :type n: int.
    :returns factorial of n
    :rtype int
    """
    return functools.reduce(operator.mul, range(1, n + 1), 1)


print(factorial(5))