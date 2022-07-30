def zero_sum(lst):
    prefix_sum = 0
    my_set = set()
    for i in range(len(lst)):
        prefix_sum += lst[i]
        if prefix_sum in my_set:
            return True
        if prefix_sum == 0:
            return True
        my_set.add(prefix_sum)
    return False


print(zero_sum([5, 3, 0]))
