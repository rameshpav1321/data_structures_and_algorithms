def search(lst, low, high, ele):
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == ele:
            return mid
        if lst[mid] > lst[low]:
            if ele < lst[mid] and ele >= lst[low]:
                high = mid-1
            else:
                low = mid+1
        else:
            if ele <= lst[high] and ele > lst[mid]:
                low = mid+1
            else:
                high = mid-1
    return "element doesn't exist"


if __name__ == "__main__":
    lst = [10, 20, 40, 60, 5, 8]
    low = 0
    high = len(lst)-1
    print(search(lst, low, high, 5))
