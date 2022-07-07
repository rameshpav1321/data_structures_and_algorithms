def sum_pair(lst, s, left, right):
    while left < right:
        if lst[left]+lst[right] == s:
            return True
        elif lst[left]+lst[right] < s:
            left += 1
        else:
            right -= 1
    return False


def triplet_sum(lst, s):
    lst.sort()
    for i in range(len(lst)-2):
        if sum_pair(lst, s-lst[i], i+1, len(lst)-1):
            return True
    return "no such triplet exists"


print(triplet_sum([1, 4, 45, 6, 10, 8], 22))
