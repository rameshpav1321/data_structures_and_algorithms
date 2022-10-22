def rain_water_trap(lst):
    l_max = []
    r_max = []
    n = len(lst)
    trapped_water = 0
    l_max.append(lst[0])
    r_max.append(lst[n-1])
    for i in range(1, len(lst)):
        l_max.append(max(lst[i], l_max[i-1]))
        r_max.append(max(lst[n-1-i], r_max[i-1]))
    r_max.reverse()
    print(l_max)
    for i in range(1, n):
        trapped_water += min(l_max[i], r_max[i])-lst[i]

    return trapped_water


print(rain_water_trap([3, 0, 1, 2, 5]))
