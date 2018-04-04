import functools


def validate(low_bound, upper_bound):
    """ Decorator, validates if given arguments are in the allowed range.

    :param low_bound: Low bound of range.
    :type low_bound: int
    :param upper_bound: Upper bound of range.
    :type upper_bound: int
    """
    def wrap_func(func):
        @functools.wraps(func)
        def inner(*args):
            res = True
            for arg in args:
                for value in arg:
                    if not low_bound <= value <= upper_bound:
                        res = False
            if res is False:
                return "Function call is not valid!"
            else:
                return func(*args)
        return inner
    return wrap_func


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    """ Print the message.
    :param pixel_values: Three numbers which represent pixel values.
    :type pixel_values: tuple
    :returns Nothing.
    :rtype None
    """
    return "Pixel created!"


print(set_pixel((0, 127, 300)))
print(set_pixel((0, 127, 30)))
print(set_pixel((0, 7, 30)))
