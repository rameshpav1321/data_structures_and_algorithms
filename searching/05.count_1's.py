def count_1s(lst, low, high, ele):
    while(low <= high):
        mid = (low+high)//2
        if lst[mid] == 0:
            low = mid+1
        elif lst[mid] == ele:
            if lst[mid] != lst[mid-1] or mid == 0:
                return mid
            else:
                high = mid-1
    return 0


if __name__ == "__main__":
    lst = [0, 0, 0, 1, 1, 1]
    low = 0
    high = len(lst)-1
    index = count_1s(lst, low, high, 1)
    if index:
        print(len(lst)-index)
    else:
        print(0)
