def more_than_nbyk(lst, k):
    occurences = len(lst)//k
    my_dict = {}
    for num in lst:
        my_dict[num] = 1+my_dict.get(num, 0)
    print(my_dict)
    for key in my_dict:
        if my_dict[key] > occurences:
            print(key)


# more_than_nbyk([30, 10, 20, 20, 10, 20, 30, 30], 4)
more_than_nbyk([30, 10, 20, 30, 30, 40, 30, 40, 30], 2)
