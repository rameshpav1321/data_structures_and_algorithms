# bubble sort is inplace sorting algorithm
def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False  # for optimization purpose
        for j in range(len(lst)-i-2):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if swapped == False:
            break
    print(lst)


bubble_sort([2, 5, 3, 5, 8, 1, 3, 9])
