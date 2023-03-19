def array_leader(lst):
    n = len(lst)
    curr_lead = lst[n-1]
    print(curr_lead)
    for i in reversed(range(n-1)):
        if lst[i] > curr_lead:
            curr_lead = lst[i]
            print(curr_lead)


array_leader([7, 10, 4, 10, 6, 5, 2])
