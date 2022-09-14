def leftmost_repeating_character(str):
    my_dict = {}
    for i in range(len(str)):
        if str[i] in my_dict:
            my_dict[str[i]][0] += 1
        else:
            my_dict[str[i]] = [1, i]
    min_pos = float('inf')
    # print(my_dict)
    for key in my_dict.keys():
        if my_dict[key][0] > 1:
            min_pos = min(min_pos, my_dict[key][1])
    if min_pos == float('inf'):
        print(-1)
    else:
        print(min_pos)


leftmost_repeating_character('geeksforgeeks')
leftmost_repeating_character('abbcc')
leftmost_repeating_character('abcd')
