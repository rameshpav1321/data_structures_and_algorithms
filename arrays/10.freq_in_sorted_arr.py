def sorted_freq(lst):
    curr_var = lst[0]
    count = 0
    for i in range(len(lst)):
        if lst[i] != curr_var:
            print(curr_var, "count is", count)
            curr_var = lst[i]
            count = 0
        if lst[i] == curr_var:
            count += 1
    print(curr_var, "count is", count)


sorted_freq([10, 10, 20, 30, 30, 40, 55, 55])
