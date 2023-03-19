def max_diff(lst):
    min_val = lst[0]
    max_diff = lst[1]-lst[0]
    for i in range(1, len(lst)):
        max_diff = max(max_diff, lst[i]-min_val)
        min_val = min(lst[i], min_val)
    return max_diff


print(max_diff([2, 3, 10, 6, 4, 8, 1]))
