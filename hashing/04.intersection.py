def intersection(nums1, nums2):
    lst = []
    set1 = set(nums1)
    set2 = set(nums2)
    for val in set1:
        if val in set2:
            lst.append(val)
    return lst


print(intersection([2, 3, 1, 4], [2, 3, 7, 8]))
