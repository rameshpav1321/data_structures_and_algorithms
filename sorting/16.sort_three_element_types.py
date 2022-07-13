def three_way_partition(lst):
    low = 0
    mid = 0
    high = len(lst)-1
    while mid <= high:
        if lst[mid] == 0:
            lst[low], lst[mid] = lst[mid], lst[low]
            low += 1
            mid += 1
        elif lst[mid] == 1:
            mid += 1
        else:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1
    print(lst)


three_way_partition([0, 1, 1, 2, 0, 1, 1, 2])
