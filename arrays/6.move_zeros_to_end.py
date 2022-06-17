# def move_zeros(lst):
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             for j in range(i+1, len(lst)):
#                 if lst[j] != 0:
#                     lst[i] = lst[j]
#                     lst[j] = 0
#                     break
#     return lst


def move_zeros(lst):
    index = 0
    temp = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            temp = lst[i]
            lst[i] = lst[index]
            lst[index] = temp
            index += 1

    return lst


if __name__ == "__main__":
    print(move_zeros([10, 3, 0, 0, 30, 408, 0, 39]))