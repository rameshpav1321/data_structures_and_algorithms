def longest_sub_arr(lst, k):
    my_dict = {}
    max_len = 0
    prefix_sum = 0
    for i in range(len(lst)):
        prefix_sum += lst[i]
        if prefix_sum == k:
            max_len = max(max_len, i+1)
            my_dict[prefix_sum] = i
        elif prefix_sum-k in my_dict:
            max_len = max(max_len, (i-my_dict[prefix_sum-k]))
            # my_dict[prefix_sum] = i
        else:
            my_dict[prefix_sum] = i
    print(max_len)


longest_sub_arr([5, 8, -4, -4, 9, - 2, 2], 0)
longest_sub_arr([3, 1, 0, 1, 8, 2, 3, 6], 5)
longest_sub_arr([8, 3, 7], 15)
