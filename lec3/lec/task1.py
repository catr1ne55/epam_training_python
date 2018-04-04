def recursive_str2int(string):
    """ Transforms the given string into it's numerical representation and returns it.

    :param string: String to transform.
    :type string: str
    :returns Numerical representation of string.
    :rtype int
    """
    if string == '':
        return 0
    else:
        current = ord(string[-1])
        length = 0
        divided = current
        while divided > 0:
            divided = divided // 10
            length += 1
        return current + recursive_str2int(string[:len(string) - 1]) * 10 ** length


print(recursive_str2int('abcd'))