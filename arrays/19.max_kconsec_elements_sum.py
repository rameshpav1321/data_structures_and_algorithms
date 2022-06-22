def k_consec_sum(lst, k):
    k_sum = 0
    for i in range(k):
        k_sum += lst[i]
    max_k_sum = k_sum
    for i in range(k, len(lst)):
        k_sum += (lst[i]-lst[i-k])
        max_k_sum = max(max_k_sum, k_sum)
    return max_k_sum


print(k_consec_sum([1, 8, 30, -5, 20, 7], 3))
