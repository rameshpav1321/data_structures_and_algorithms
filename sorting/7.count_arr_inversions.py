def count_and_merge(lst, left, mid, right):
    lst1 = []
    lst2 = []
    for i in range(left, mid+1):
        lst1.append(lst[i])
    for i in range(mid+1, right+1):
        lst2.append(lst[i])
    i, j, k, res = 0, 0, left, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
            k += 1
        else:
            res = res+(len(lst1)-i)
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
    return res


def arr_inversions(lst, left, right):
    res = 0
    if right > left:
        mid = left+(right-left)//2
        res += arr_inversions(lst, left, mid)
        res += arr_inversions(lst, mid+1, right)
        res += count_and_merge(lst, left, mid, right)
    return res


print(arr_inversions([2, 4, 1, 3, 5], 0, 4))
