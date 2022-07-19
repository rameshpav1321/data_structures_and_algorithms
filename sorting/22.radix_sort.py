def count_sort(lst, lst_len, exp):
    count = [0]*10
    output = [0]*lst_len
    for i in range(lst_len):
        count[(lst[i]//exp) % 10] += 1
    # print("count1", count)
    for i in range(1, 10):
        count[i] = count[i]+count[i-1]
    # print("count2", count)
    for i in range(lst_len-1, -1, -1):
        output[count[(lst[i]//exp) % 10] - 1] = lst[i]
        count[(lst[i]//exp) % 10] -= 1
    lst = output
    return lst


def radix_sort(lst, lst_len):
    max_ele = max(lst)
    exp = 1
    while max_ele//exp > 0:
        res = count_sort(lst, lst_len, exp)
        exp *= 10
    print(res)


radix_sort([319, 212, 6, 8, 100, 50], 6)
