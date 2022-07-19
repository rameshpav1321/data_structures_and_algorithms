def lpartition(lst, low, high):
    pivot = lst[high][0]
    i = low-1
    for j in range(low, high):
        if lst[j][0] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1


def quick_sort(lst, low, high):
    if low < high:
        p = lpartition(lst, low, high)
        quick_sort(lst, low, p-1)
        quick_sort(lst, p+1, high)
    return lst


print(quick_sort([[15, 18], [2, 6], [1, 3]], 0, 2))
