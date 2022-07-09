def insertion_sort(lst):
    key = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    print(lst)


insertion_sort([3, 5, 2, 5, 3, 7, 1])
