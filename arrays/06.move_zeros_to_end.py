# def move_zeros(lst):
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             for j in range(i+1, len(lst)):
#                 if lst[j] != 0:
#                     lst[i] = lst[j]
#                     lst[j] = 0
#                     break
#     return lst


# def moveZeroes(self, lst: List[int]) -> None:
#         index=0
#         temp=float('inf')
#         for i in range(len(lst)):
#             if lst[i]!=0:
#                 lst[index],lst[i]=lst[i],lst[index]
#                 index+=1
#             else:
#                 if temp!=0:
#                     index=i
#                     temp=0
#         return lst

def move_zeros(lst):
    index = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i], lst[index] = lst[index], lst[i]
            index += 1
    return lst


if __name__ == "__main__":
    print(move_zeros([10, 3, 0, 0, 30, 408, 0, 39]))
