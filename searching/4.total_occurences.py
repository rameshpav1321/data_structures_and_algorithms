from first_occurence import first_occurence
from last_occuring import last_occurence

# def first_occurence(lst, low, high, ele):
#     if low <= high:
#         mid = (low+high)//2
#     else:
#         return "element doesn't exist"
#     if lst[mid] == ele:
#         if lst[mid] != lst[mid-1] or mid == 0:
#             return mid
#         else:
#             return first_occurence(lst, low, mid-1, ele)
#     elif ele < lst[mid]:
#         return first_occurence(lst, low, mid-1, ele)
#     else:
#         return first_occurence(lst, mid+1, high, ele)


# def last_occurence(lst, low, high, ele):
#     if low <= high:
#         mid = (low+high)//2
#     else:
#         return "element doesn't exist"
#     if lst[mid] == ele:
#         if mid == len(lst)-1 or lst[mid] != lst[mid+1]:
#             return mid
#         else:
#             return last_occurence(lst, mid+1, high, ele)
#     elif ele < lst[mid]:
#         return last_occurence(lst, low, mid-1, ele)
#     else:
#         return last_occurence(lst, mid+1, high, ele)


if __name__ == "__main__":
    lst = [10, 20, 20, 20, 20, 30, 40]
    low = 0
    high = len(lst)-1
    first_index = first_occurence(lst, low, high, 20)
    last_index = last_occurence(lst, low, high, 20)
    print((last_index-first_index)+1)
