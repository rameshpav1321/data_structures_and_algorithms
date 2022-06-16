def array_reverse(lst):
    low_index = 0
    high_index = len(lst)-1
    temp = 0
    for i in range(len(lst)//2):
        temp = lst[low_index]
        lst[low_index] = lst[high_index]
        lst[high_index] = temp
        low_index += 1
        high_index -= 1
    return lst


if __name__ == "__main__":
    lst = list(map(int, input("enter the values for the list: ").split()))
    print(array_reverse(lst))
