#  def removeDuplicates(self, lst: List[int]) -> int:
#         index=1
#         for i in range(1,len(lst)):
#             if lst[i]!=lst[i-1]:
#                 lst[index]=lst[i]
#                 index+=1
#         return index

def remove_dup(lst):
    temp = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[temp-1]:
            lst[temp] = lst[i]
            temp += 1
    return lst[:temp]


if __name__ == "__main__":
    lst = list(map(int, input("enter the values for the list: ").split()))
    print(remove_dup(lst))
