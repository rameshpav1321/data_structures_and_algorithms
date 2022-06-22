def prefix_sum(lst, st, en):
    prefix_sum_arr = []
    prefix_sum = 0
    for i in range(len(lst)):
        prefix_sum += lst[i]
        prefix_sum_arr.append(prefix_sum)
    if st != 0:
        return prefix_sum_arr[en]-prefix_sum_arr[st-1]
    else:
        return prefix_sum_arr[en]


print(prefix_sum([2, 8, 3, 9, 6, 5, 4], 1, 3))
