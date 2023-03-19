def selection_sort(lst):
    for i in range(len(lst)):
        min_ind = i
        for j in range(i+1, len(lst)):
            if lst[min_ind] > lst[j]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]
    print(lst)


selection_sort([2, 4, 5, 2, 3, 9, 7])
