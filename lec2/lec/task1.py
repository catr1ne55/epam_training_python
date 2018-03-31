def intersect(*args):
    intersect_set = set()
    for a0 in args:
        cont = True
        for a00 in a0:
            for a in args:
                if a != a0 and a00 not in a:
                    cont = False
            if cont:
                intersect_set.add(a00)
    return list(intersect_set)


def better_intersect(*args): # doesn't work with different types of args !!!
    inter_set = set()
    min_arg = min(args)
    for m in min_arg:
        cond = True
        for a in args:
            if m not in a:
                cond = False
        if cond:
            inter_set.add(m)
    return list(inter_set)


def union(*args):
    union_set = set()
    for a in args:
        for a1 in a:
            if a1 not in union_set:
                union_set.add(a1)
    return list(union_set)


print(union("sam", "spac", "asdt"))
print(union("asd", "123"))

print(intersect("123","14"))
print(intersect("abs","aabc"))
print(intersect([1,2,3], [1,4]))
print(intersect("plpl", ("p", "a")))

print(better_intersect("123","14"))
print(better_intersect("abs","aabc"))
print(better_intersect([1,2,3], [1,4]))
print(better_intersect("plpl", "asddw"))
print(better_intersect("plpl", ("p", "l")))