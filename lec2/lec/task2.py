def str2int(string):
    """Transforms the given string into it's numerical representation and returns it."""
    num = 0
    for s in string:
        cur = ord(s)
        l = 0
        div = cur
        while div > 0:
            div = div // 10
            l += 1
        num = num * 10 ** l + cur
    return num


print(str2int('abcd'))
print(str2int('asdcbhffds'))
