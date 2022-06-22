def majority_element(lst):
    maj_ele = 0
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[maj_ele]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_ele = i
            count = 1
    return maj_ele


if __name__ == "__main__":
    lst = [6, 8, 7, 7, 8]
    res = majority_element(lst)
    count = 0
    for i in range(len(lst)):
        if lst[res] == lst[i]:
            count += 1
    if count > len(lst)//2:
        print(res, lst[res])
    else:
        print('no majority element')
