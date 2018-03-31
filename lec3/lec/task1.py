def rstr2int(string):
    """ Transforms the given string into it's numerical representation and returns it."""
    if string == '':
        return 0
    else:
        cur = ord(string[-1])
        l = 0
        div = cur
        while div > 0:
            div = div // 10
            l += 1
        return cur + rstr2int(string[:len(string) - 1]) * 10 ** l


print(rstr2int('abcd'))