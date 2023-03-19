def sum_pair(lst, s):
    my_set = set()
    for i in range(len(lst)):
        if s-lst[i] in my_set:
            return True
        else:
            my_set.add(lst[i])
    return False


print(sum_pair([8, 3, 4, 5], 6))
