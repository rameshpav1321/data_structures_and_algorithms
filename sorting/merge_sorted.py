def merge_sorted(lst, low, mid, high):
    lst1 = []
    lst2 = []
    for i in range(low, mid+1):
        lst1.append(lst[i])
    for i in range(mid+1, high+1):
        lst2.append(lst[i])
    i = 0
    j = 0
    k = low
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
            k += 1
        else:
            lst[k] = lst2[j]
            j += 1
            k += 1
    while i < len(lst1):
        lst[k] = lst1[i]
        i += 1
        k += 1
    while j < len(lst2):
        lst[k] = lst2[j]
        j += 1
        k += 1
    # print(lst)


merge_sorted([5, 10, 30, 7, 15], 0, 2, 4)
