def bucket_sort(lst, lst_len, bkts):
    buckets = [[] for _ in range(bkts)]
    max_ele = max(lst)
    max_ele += 1
    res = []
    for i in range(lst_len):
        buckets[lst[i]*bkts//max_ele].append(lst[i])
    lst.clear()
    for bucket in buckets:
        bucket.sort()
        lst += bucket
    print(lst)


bucket_sort([30, 40, 10, 80, 5, 12, 70], 7, 4)
