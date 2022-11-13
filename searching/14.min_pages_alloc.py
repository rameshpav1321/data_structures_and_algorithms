def min_pages_alloc(lst, stud):
    arr_mx,arr_sum=max(lst),sum(lst)
    low,high=arr_mx,arr_sum
    res = 0
    while low <= high:
        # print(low, high)
        mid = (low+high)//2
        stud_aux = 1
        sum_aux = 0
        for i in range(len(lst)):
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
