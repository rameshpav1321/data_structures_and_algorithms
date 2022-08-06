from re import I


def longest_common_sum(lst1, lst2):
    temp = []
    for i in range(len(lst1)):
        temp.append(lst1[i]-lst2[i])
    my_dict = {}
    prefix_sum = 0
    max_len = 0
    for i in range(len(temp)):
        prefix_sum += temp[i]
        if prefix_sum == 0:
            max_len = max(max_len, i+1)
            my_dict[prefix_sum] = i
        elif prefix_sum in my_dict:
            max_len = max(max_len, i-my_dict[prefix_sum])
        else:
            my_dict[prefix_sum] = i
    print(max_len)


longest_common_sum([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1])
