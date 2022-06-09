def subset_sum(lst, s, curr=[], i=0):
    print(len(lst))
    count = 0
    if i == len(lst):
        lst_sum = sum(curr)
        if s == lst_sum:
            count += 1
        return
    subset_sum(lst, s, curr, i+1)
    subset_sum(lst, s, curr.append(lst[i]), i+1)
    return count


if __name__ == "__main__":
    lst = (input("enter the values: ")).split()
    s = int(input("enter the sum value to match: "))
    print(subset_sum(lst, s))
