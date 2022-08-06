def longest_sub_arr(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = -1
    prefix_sum = 0
    my_dict = {}
    max_len = 0
    for i in range(len(lst)):
        prefix_sum += lst[i]
        if prefix_sum == 0:
            max_len = max(max_len, i+1)
            my_dict[prefix_sum] = i
        elif prefix_sum in my_dict:
            max_len = max(max_len, i-my_dict[prefix_sum])
        else:
            my_dict[prefix_sum] = i
    print(max_len)
