def max_occuring(l_lst, r_lst):
    lst = [0]*1000
    for i in range(len(l_lst)):
        lst[l_lst[i]] = 1
        lst[r_lst[i]+1] = -1
    max_ele = lst[0]
    res = 0
    for i in range(1, len(lst)):
        lst[i] += lst[i-1]
        if max_ele < lst[i]:
            max_ele = lst[i]
            res = i
    return res


print(max_occuring([1, 2, 3], [3, 5, 7]))
