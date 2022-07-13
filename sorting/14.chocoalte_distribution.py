def distribute_chocolates(lst, n):
    lst.sort()
    min_val = float('infinity')
    for i in range(len(lst)-n+1):
        min_val = min(min_val, (lst[i+n-1]-lst[i]))
    for i in range(len(lst)-n+1):
        diff = lst[i+n-1]-lst[i]
        if diff == min_val:
            return lst[i:i+n], diff


print(distribute_chocolates([3, 4, 9, 7, 9, 1, 12, 56], 5))
