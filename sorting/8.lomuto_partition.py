def lomuto_partition(lst, low, high, pivot_index):
    if pivot_index != high:
        lst[high], lst[pivot_index] = lst[pivot_index], lst[high]
    pivot = lst[high]
    i = low-1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    print(lst)


lomuto_partition([10, 80, 90, 40, 50, 70], 0, 5, 5)
