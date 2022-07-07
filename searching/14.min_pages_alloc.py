def min_pages_alloc(lst, stud):
    le = len(lst)
    sum = 0
    arr_mx = 0
    for i in range(le):
        sum += lst[i]
        arr_mx = max(lst[i], arr_mx)
    low = arr_mx
    high = sum
    res = 0
    while low <= high:
        # print(low, high)
        mid = (low+high)//2
        stud_aux = 1
        sum_aux = 0
        for i in range(le):
            if sum_aux+lst[i] > mid:
                stud_aux += 1
                sum_aux = lst[i]
            else:
                sum_aux += lst[i]
        # print(stud_aux)
        if stud_aux <= stud:
            # print("mid:", mid)
            res = mid
            high = mid-1
        else:
            # print("inside else:", mid)
            low = mid+1
    print("minimum allocated pages:", res)


min_pages_alloc([10, 20, 10, 30], 2)
