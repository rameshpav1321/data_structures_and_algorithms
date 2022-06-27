def longest_even_odd(lst):
    res = 1
    curr = 1
    for i in range(1, len(lst)):
        if (lst[i] % 2 == 0 and lst[i-1] % 2 != 0) or (lst[i] % 2 != 0 and lst[i-1] % 2 == 0):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res


print(longest_even_odd([5, 10, 20, 6, 3, 8]))
