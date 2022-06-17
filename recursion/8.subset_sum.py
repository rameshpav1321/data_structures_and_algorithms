def subset_sum(lst, s, curr=[], i=0, count=0):
    if i == len(lst):
        lst_sum = sum(curr)
        if s == lst_sum:
            count += 1
        return count
    count = subset_sum(lst, s, curr, i+1, count)
    count = subset_sum(lst, s, curr+[lst[i]], i+1, count)
    return count


if __name__ == "__main__":
    lst = list(map(int, input("enter the values: ").split()))
    s = int(input("enter the sum value to match: "))
    count = subset_sum(lst, s)
    print(count)
