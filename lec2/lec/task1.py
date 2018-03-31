def intersect(*args):
    """ Returns a new list with elements that are common to all sets."""
    intersect_set = set()
    for cur_arg in args:
        cont = True
        for elem in cur_arg:
            for other_arg in args:
                if other_arg != cur_arg and elem not in other_arg:
                    cont = False
            if cont:
                intersect_set.add(elem)
    return list(intersect_set)


def better_intersect(*args):
    """ Returns a new list with elements that are common to all sets. """
    inter_set = set()
    min_arg = sorted(args, key=len)[0] # find the minimal set and compare it's elements to other sets' elements
    for elem in min_arg:
        cond = True
        for arg in args:
            if elem not in arg:
                cond = False
        if cond:
            inter_set.add(elem)
    return list(inter_set)


def union(*args):
    """ Returns a new list with distinct elements from all the sets."""
    union_set = set()
    for arg in args:
        for elem in arg:
           union_set.add(elem)
    return list(union_set)


print(union("sam", "spac", "asdt"))
print(union("asd", "123"))

print(intersect("123","14"))
print(intersect("abs","aabc"))
print(intersect([1,2,3], [1,4]))
print(intersect("plpl", ("p", "a")))
print(intersect([],[]))

print(better_intersect("123","14"))
print(better_intersect("abs","aabc"))
print(better_intersect([1,2,3], [1,4]))
print(better_intersect("plpl", "asddw"))
print(better_intersect("plpl", ("p", "l")))
print(better_intersect("plpl", ("p", "l"), ['p0', 'fdsdf', 'slsjf']))