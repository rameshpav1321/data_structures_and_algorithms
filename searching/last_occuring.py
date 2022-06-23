def last_occurence(lst, low, high, ele):
    if low <= high:
        mid = (low+high)//2
    else:
        return "element doesn't exist"
    if lst[mid] == ele:
        if mid == len(lst)-1 or lst[mid] != lst[mid+1]:
            return mid
        else:
            return last_occurence(lst, mid+1, high, ele)
    elif ele < lst[mid]:
        return last_occurence(lst, low, mid-1, ele)
    else:
        return last_occurence(lst, mid+1, high, ele)


if __name__ == "__main__":
    lst = [20, 20, 20, 20]
    low = 0
    high = len(lst)-1
    print(last_occurence(lst, low, high, 20))
