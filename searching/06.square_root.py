# O(n)
# def square_root(n):
#     i = 1
#     while(i*i <= n):
#         i += 1
#     return i-1

# O(logn)
def square_root(n):
    low = 1
    high = n
    while(low <= high):
        mid = (low+high)//2
        mid_sq = mid**2
        if n == mid_sq:
            return mid
        elif mid_sq > n:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans


print(square_root(89))
