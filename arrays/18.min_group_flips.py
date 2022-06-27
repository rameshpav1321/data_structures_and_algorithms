def min_grp_flips(lst):
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            if lst[i] != lst[0]:
                print("flip from", i, "to ", end='')
            else:
                print(i-1)
    if lst[len(lst)-1] != lst[0]:
        print(len(lst)-1)


min_grp_flips([1, 0, 0, 0, 0, 1, 0, 0, 1, 0])
