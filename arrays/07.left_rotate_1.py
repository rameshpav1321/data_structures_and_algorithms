# another way to solve is to reverse elements: O(1) space
# array_reverse(lst,0,n-1)
# array_reverse(lst,n,le-1)
# array_reverse(lst,0,le-1)

def left_rotate(lst, n):
    le = len(lst)
    temp = []
    for i in range(n):
        temp.append(lst[i])
    for i in range(n, len(lst)):
        lst[i-n] = lst[i]
    for i in range(n):
        lst[(le-n)+i] = temp[i]
    return lst


print(left_rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
