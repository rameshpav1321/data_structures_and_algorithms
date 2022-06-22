def sub_arr_sum(lst, s):
    curr_sum = lst[0]
    st = 0
    for en in range(1, len(lst)):
        while curr_sum > s and st <= en-1:
            curr_sum -= lst[st]
            st += 1
        if curr_sum == s:
            return True
        if curr_sum < s:
            curr_sum += lst[en]
    return curr_sum == s


print(sub_arr_sum([15, 2, 4, 8, 9, 5, 10, 23], 11))
