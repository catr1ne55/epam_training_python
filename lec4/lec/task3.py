import functools


def sum_string(sentences):
    """ Counts length of all items in sentences.

    :param sentences: A list f strings, where we count lengths.
    :type sentences: list.
    :returns Number of summary length.
    :rtype int.
    """
    return functools.reduce(lambda x, y: x + len(y), sentences, 0)


print(sum_string(["test", "twoo", "ddsd"]))