def largest_element(lst):
    res = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[res]:
            res = i
    return res, lst[res]


if __name__ == "__main__":
    lst = list(map(int, input("enter the values for the list: ").split()))
    print(largest_element(lst))
