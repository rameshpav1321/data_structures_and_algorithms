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


def search(lst, ele):
    if lst[0] == ele:
        return 0
    i = 1
    while(lst[i] < ele):
        i *= 2
    if lst[i] == ele:
        return i
    else:
        return binary_search(lst, i//2+1, i-1, ele)


print(search([1, 2, 3, 5, 5], 4))
