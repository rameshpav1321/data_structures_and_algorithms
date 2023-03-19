def union(lst1, lst2):
    res = lst1+lst2
    res = set(res)
    print(res, len(res))


union([2, 8, 3, 5, 6], [4, 8, 3, 6, 1])
