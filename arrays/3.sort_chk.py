def sort_chk(lst):
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return "array is not sorted in ascending order"
    return "array is sorted"


if __name__ == "__main__":
    lst = list(map(int, input("enter the values for the list: ").split()))
    print(sort_chk(lst))
