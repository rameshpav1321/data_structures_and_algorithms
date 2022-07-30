def k_sum(lst, k):
    prefix_sum = 0
    my_set = set()
    for i in range(len(lst)):
        prefix_sum += lst[i]
        if prefix_sum-k in my_set:
            return True
        if prefix_sum == k:
            return True
        my_set.add(prefix_sum)
    return False


print(k_sum([5, 8, 0], 0))
