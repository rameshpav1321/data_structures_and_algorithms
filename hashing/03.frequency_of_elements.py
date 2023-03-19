def element_frequency(lst):
    my_dict = {}
    for i in range(len(lst)):
        my_dict[lst[i]] = 1+my_dict.get(lst[i], 0)
        # if lst[i] in my_dict:
        #     my_dict[lst[i]] += 1
        # else:
        #     my_dict[lst[i]] = 1
    for key, val in my_dict.items():
        print(f"Count for {key} is {val}")


element_frequency([10, 0, 20, 3, 4, 2, 3, 10])
