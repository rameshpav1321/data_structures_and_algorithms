# def merge_sorted(lst, low, mid, high):
#     lst1 = []
#     lst2 = []
#     for i in range(low, mid+1):
#         lst1.append(lst[i])
#     for i in range(mid+1, high+1):
#         lst2.append(lst[i])
#     i = 0
#     j = 0
#     k = low
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             lst[k] = lst1[i]
#             i += 1
#             k += 1
#         else:
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


# def merge_sort(lst, low, high):
#     if low < high:
#         mid = (low+high)//2
#         merge_sort(lst, low, mid)
#         merge_sort(lst, mid+1, high)
#         merge_sorted(lst, low, mid, high)

def min_diff(lst):
    # low = 0
    # high = len(lst)-1
    # merge_sort(lst, low, high)
    lst.sort()
    min_diff = float('infinity')
    for i in range(1, len(lst)):
        min_diff = min(min_diff, abs(lst[i]-lst[i-1]))
    print(min_diff)


min_diff([10, 7, 1, 4])
