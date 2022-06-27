def first_occurence(lst, low, high, ele):
    if low <= high:
        mid = (low+high)//2
    else:
        return "element doesn't exist"
    if lst[mid] == ele:
        if lst[mid] != lst[mid-1] or mid == 0:
            return mid
        else:
            return first_occurence(lst, low, mid-1, ele)
    elif ele < lst[mid]:
        return first_occurence(lst, low, mid-1, ele)
    else:
        return first_occurence(lst, mid+1, high, ele)


if __name__ == "__main__":
    lst = [20, 20, 20, 20]
    low = 0
    high = len(lst)-1
    print(first_occurence(lst, low, high, 20))
