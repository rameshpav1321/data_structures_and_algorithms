def sum_pair(lst, s):
    left = 0
    right = len(lst)-1
    while left < right:
        if lst[left]+lst[right] == s:
            return True
        elif lst[left]+lst[right] < s:
            left += 1
        else:
            right -= 1
    return "no pair that matches the given exists"


print(sum_pair([2, 3, 7, 8, 11], 14))
