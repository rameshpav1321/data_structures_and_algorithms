def max_sub_array_sum(lst):
    max_sum = lst[0]
    res = lst[0]
    for i in range(1, len(lst)):

        max_sum = max(max_sum+lst[i], lst[i])
        res = max(res, max_sum)
    return res


# print(max_sub_array_sum([2, 3, -8, 7, -1, 2, 3]))
print(max_sub_array_sum([-5, 1, -2, 3, -1, 2, -2]))
