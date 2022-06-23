def binary_search(lst, low, high, ele):
    if low <= high:
        mid = (low+high)//2
    else:
        return "element doesn't exist"
    if lst[mid] == ele:
        return lst[mid], mid
    elif ele < lst[mid]:
        return binary_search(lst, low, mid-1, ele)
    else:
        return binary_search(lst, mid+1, high, ele)


# def binary_search(lst, low, high, ele):
#     while(low <= high):
#         mid = (low+high)//2
#         if lst[mid] == ele:
#             return lst[mid], mid
#         elif ele < lst[mid]:
#             high = mid-1
#         else:
#             low = mid+1
#     return "element doesn't exist"


if __name__ == "__main__":
    lst = [10, 20, 48, 68, 78]
    low = 0
    high = len(lst)-1
    print(binary_search(lst, low, high, 20))
