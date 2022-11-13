# # from collections import defaultdict
# def repeated_element(lst):
#     # my_dict=defaultdict(int)
#     my_dict = {}
#     for i in range(len(lst)):
#         if lst[i] in my_dict.keys():
#             my_dict[lst[i]] += 1
#         else:
#             my_dict[lst[i]] = 1
#     for key, value in my_dict.items():
#         if value > 1:
#             print(key)

def repeated_element(lst):
    one_jmp, two_jmp = 0, 0
    while True:
        one_jmp = lst[one_jmp]
        two_jmp = lst[lst[two_jmp]]
        if one_jmp == two_jmp:
            print(one_jmp, two_jmp)
            break
    one_jmp_left = 0
    while True:
        one_jmp = lst[one_jmp]
        one_jmp_left = lst[one_jmp_left]
        if one_jmp_left == one_jmp:
            return one_jmp_left


print(repeated_element([2, 3, 8, 5, 6, 6, 4, 1, 7]))
