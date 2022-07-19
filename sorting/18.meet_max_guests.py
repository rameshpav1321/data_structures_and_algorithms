# def meet_max_guests(lst1, lst2):
#     lst = []
#     for i in range(len(lst1)):
#         lst.append([lst1[i], lst2[i]])
#     lst.sort()
#     print(lst)
#     res = 0
#     count = 1
#     meets = 1
#     for i in range(1, len(lst)):
#         if lst[res][0] <= lst[i][0] <= lst[res][1]:
#             lst[res][1] = max(lst[res][1], lst[i][1])
#             count += 1
#             meets = max(count, meets)
#         else:
#             res += 1
#             count = 1
#             lst[res] = lst[i]
#     print(lst[:res+1])
#     print(meets)

def meet_max_guests(arr, dep):
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    res = 1
    curr = 1
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1
        res = max(res, curr)
    print(res)


meet_max_guests([900, 940, 950, 1100, 1500, 1800], [
                910, 1200, 1120, 1130, 1900, 2000])
