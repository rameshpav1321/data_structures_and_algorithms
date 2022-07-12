from random import randint


def hpartition(lst, low, high):
    i = low-1
    j = high+1
    p = randint(low, high)
    print(p)
    pivot = lst[p]
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
            return j
        lst[i], lst[j] = lst[j], lst[i]


def quick_sort(lst, low, high):
    if low < high:
        p = hpartition(lst, low, high)
        quick_sort(lst, low, p)
        quick_sort(lst, p+1, high)
    return lst


print(quick_sort([5, 1, 1, 2, 0, 0], 0, 5))
