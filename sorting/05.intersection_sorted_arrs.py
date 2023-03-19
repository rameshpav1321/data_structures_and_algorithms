def intersection(lst1, lst2):
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):

        if i >= 0 and lst1[i] == lst1[i-1]:
            i += 1
            continue
        elif lst1[i] < lst2[j]:
            i += 1
        elif lst1[i] > lst2[j]:
            j += 1
        else:
            print(lst1[i])
            i += 1
            j += 1


intersection([3, 5, 10, 10, 10, 15, 15, 20], [5, 10, 10, 15, 30])
