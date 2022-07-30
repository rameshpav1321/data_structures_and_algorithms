def count_distinct(lst):
    # my_dict = {}
    # for i in range(len(lst)):
    #     if lst[i] in my_dict:
    #         my_dict[lst[i]] += 1
    #     else:
    #         my_dict[lst[i]] = 1
    # print(my_dict, len(my_dict))
    print(len(set(lst)))


count_distinct([10, 20, 10, 20, 30])
