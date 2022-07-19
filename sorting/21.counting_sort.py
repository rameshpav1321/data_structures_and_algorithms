def count_sort(lst, lst_len, k):
    count = [0]*k
    for i in range(len(lst)):
        count[lst[i]] += 1
    for i in range(1, k):
        count[i] = count[i]+count[i-1]
    output = [0]*lst_len
    for i in range(lst_len-1, -1, -1):
        output[count[lst[i]]-1] = lst[i]
        count[lst[i]] -= 1
    lst = output
    print(lst)


count_sort([1, 4, 3, 2, 5, 1], 6, 6)
