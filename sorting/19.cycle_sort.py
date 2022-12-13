def cycle_sort(lst):
    swaps,pos,item = 0,0,0
    for cycle_start in range(len(lst)-1):
        pos = cycle_start
        item = lst[cycle_start]
        for i in range(cycle_start+1, len(lst)):
            if lst[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == lst[pos]:
            pos += 1
        item, lst[pos] = lst[pos], item
        swaps += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start+1, len(lst)):
                if lst[i] < item:
                    pos += 1
            while item == lst[pos]:
                pos += 1
            item, lst[pos] = lst[pos], item
            swaps += 1
            print(lst, swaps)
    


cycle_sort([1, 8, 3, 9, 10, 10, 2, 4])
