def union(lst1, lst2):
    i, j = 0, 0
    while(i < len(lst1) and j < len(lst2)):
        if i > 0 and lst1[i] == lst1[i-1]:
            continue
        elif j > 0 and lst2[j] == lst2[j-1]:
            continue
        elif lst1[i] < lst2[j]:
            print(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            print(lst2[j])
            j += 1
        else:
            print(lst1[i])
            i += 1
            j += 1
    while i < len(lst1):
        if i > 0 and lst1[i] != lst1[i-1]:
            print(lst1[i])
            i += 1
    while j < len(lst2):
        if j > 0 and lst2[j] != lst2[j-1]:
            print(lst2[j])
            j += 1


union([3, 8, 10], [2, 8, 9, 10, 15])
