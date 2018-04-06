import functools


def count_test(sentences):
    """ Counts number of occurrence "test" in sentences.

    :param sentences: A list f strings, where we count occurrences of "test".
    :type sentences: list.
    :returns Number of "test" in sentences.
    :rtype int.
    """
    return functools.reduce(lambda x, y: x + y.count("test"), sentences, 0)


print(count_test(["test", "twoo", "ddsdtest"]))