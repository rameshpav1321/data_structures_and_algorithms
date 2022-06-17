def consec_ones(lst):
    max_count = 0
    curr_var = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] != curr_var:
            count += 1
            max_count = max(count, max_count)
        if lst[i] == 0:
            count = 0
    return max_count


print(consec_ones([0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
