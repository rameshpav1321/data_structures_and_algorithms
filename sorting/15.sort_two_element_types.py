# def merge(lst, low, mid, high):
#     lst1 = []
#     lst2 = []
#     for i in range(low, mid+1):
#         lst1.append(lst[i])
#     for i in range(mid+1, high+1):
#         lst2.append(lst[i])
#     i = 0
#     j = 0                                     This solution uses merge sort to perform the task                                          w
#     k = low                                   where as efficient way is to use lomuto or hoare partition.
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < 0:
#             lst[k] = lst1[i]
#             i += 1
#             k += 1
#         elif lst2[j] < 0:
#             lst[k] = lst2[j]
#             j += 1
#             k += 1
#         else:
#             lst[k] = lst1[i]
#             i += 1
#             k += 1
#             lst[k] = lst2[j]
#             j += 1
#             k += 1
#     while i < len(lst1):
#         lst[k] = lst1[i]
#         i += 1
#         k += 1
#     while j < len(lst2):
#         lst[k] = lst2[j]
#         j += 1
#         k += 1

# def sort(lst, low, high):
#     if low < high:
#         mid = (low+high)//2
#         sort(lst, low, mid)
#         sort(lst, mid+1, high)
#         merge(lst, low, mid, high)
#     return lst
def hoare_partition(lst, low, high):
    i = low-1
    j = high+1
    while True:
        while True:
            i += 1
            if lst[i] >= 0:
                break
        while True:
            j -= 1
            if lst[j] < 0:
                break
        if i >= j:
            print(lst)
            return
        lst[i], lst[j] = lst[j], lst[i]


hoare_partition([13, -12, 18, -10, 0, 0], 0, 5)
