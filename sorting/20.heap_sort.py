def heapify(lst, lst_len, curr_node):
    largest = curr_node
    left = 2*curr_node+1
    right = 2*curr_node+2
    if left < lst_len and lst[left] > lst[largest]:
        largest = left
    if right < lst_len and lst[right] > lst[largest]:
        largest = right
    if largest != curr_node:
        lst[curr_node], lst[largest] = lst[largest], lst[curr_node]
        heapify(lst, lst_len, largest)


def heap_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len-2//2, -1, -1):
        heapify(lst, lst_len, i)
    for i in range(lst_len-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    print(lst)


heap_sort([12, 11, 13, 5, 6, 7])
