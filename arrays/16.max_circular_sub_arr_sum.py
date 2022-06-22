# o(n**2): idea is to find all sub arrays including circular starting with each list element

# def max_circular_sum(lst):
#     res = lst[0]
#     for i in range(len(lst)):
#         curr_sum = lst[i]
#         curr_max = lst[i]
#         for j in range(1, len(lst)):
#             index = (i+j) % len(lst)
#             curr_sum += lst[index]
#             curr_max = max(curr_max, curr_sum)
#         res = max(res, curr_max)
#     return res


# o(n): idea is to calculate max_arr_sum and max_cir_sum, return max of both
# for calculating max_cir_sum idea is to find total arr sum and subtract min_arr_sum
def max_arr_sum(lst):
    res = lst[0]
    max_sum = lst[0]
    for i in range(1, len(lst)):
        max_sum = max(max_sum+lst[i], lst[i])
        res = max(res, max_sum)
    return res


def max_cir_sum(lst):
    res = 0
    arr_sum = 0
    max_sum = max_arr_sum(lst)
    for i in range(len(lst)):
        arr_sum += lst[i]
        lst[i] = -lst[i]
    min_sum = max_arr_sum(lst)
    max_cir_sum = arr_sum+min_sum
    res = max(max_sum, max_cir_sum)
    return res


print(max_cir_sum([5, -2, 3, 4]))
