# def count_distinct_window(lst, size):
#     my_dict = {}
#     index = 0
#     count = 0
#     i = 0
#     while(i < len(lst)):
#         my_dict[lst[i]] = 1+my_dict.get(lst[i], 0)
#         count += 1
#         if count == size:
#             print(len(my_dict))
#             my_dict = {}
#             index += 1
#             i = index
#             count = 0
#         else:
#             i += 1

def count_distinct_window(lst, size):
    my_dict = {}
    res = []
    for i in range(size):
        my_dict[lst[i]] = 1+my_dict.get(lst[i], 0)
    res.append(len(my_dict))
    for i in range(size, len(lst)):
        my_dict[lst[i-size]] -= 1
        if my_dict[lst[i-size]] == 0:
            del my_dict[lst[i-size]]
        my_dict[lst[i]] = 1+my_dict.get(lst[i], 0)
        res.append(len(my_dict))
    print(res)


count_distinct_window([10, 20, 20, 10, 30, 40, 10], 4)
