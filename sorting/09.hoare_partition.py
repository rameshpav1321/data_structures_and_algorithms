def hoare_partition(lst, low, high):
    i = low-1
    j = high+1
    pivot = lst[low]
    while True:
        while True:
            i += 1
            if lst[i] >= pivot:
                break
        while True:
            j -= 1
            if lst[j] <= pivot:
                break
        if i >= j:
            print(lst)
            return j
        lst[i], lst[j] = lst[j], lst[i]


hoare_partition([3, 1, 2, 5, 5], 0, 4)
