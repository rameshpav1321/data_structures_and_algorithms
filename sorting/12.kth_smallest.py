def lpartition(lst, low, high):
    pivot = lst[high]
    i = low-1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1


def kth_smallest(lst, k):
    low = 0
    high = len(lst)-1
    while low <= high:
        p = lpartition(lst, low, high)
        if p == k-1:
            return lst[p]
        elif p < k-1:
            low = p+1
        else:
            high = p-1
    return "no such element exists"


print(kth_smallest([10, 4, 5, 8, 11, 6, 26], 5))
