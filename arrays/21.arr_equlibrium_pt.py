def arr_equilibrium(lst):
    left_sum = 0
    total_sum = 0
    for i in range(len(lst)):
        total_sum += lst[i]
    for i in range(len(lst)):
        if left_sum == total_sum-lst[i]:
            return f"array has a equilibrium element at:{i} "
        else:
            left_sum += lst[i]
            total_sum -= lst[i]
    return "array does not have an equilibrium element"


print(arr_equilibrium([3, 4, 8, -9, 20, 6]))
