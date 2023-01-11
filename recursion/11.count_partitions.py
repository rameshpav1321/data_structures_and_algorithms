# No.of ways n things can be partioned using upto m values
def count_partitions(n,m):
    if n==0:
        return 1
    if m==0 or n<1:
        return 0
    return count_partitions(n-m,m)+count_partitions(n,m-1)