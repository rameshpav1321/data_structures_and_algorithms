def median_sorted_arr(nums1, nums2):
    lst1 = nums1
    lst2 = nums2
    if len(lst1) > len(lst2):
        lst1, lst2 = lst2, lst1
    len1, len2 = len(lst1), len(lst2)
    left, right = 0, len1-1
    while left <= right:
        i = (left+right)//2
        j = (len1+len2+1)//2-i
        max1 = float('inf')if i == len1 else lst1[i]
        min1 = float('-inf')if i == 0 else lst1[i-1]
        max2 = float('inf')if j == len2 else lst2[j]
        min2 = float('-inf')if j == 0 else lst2[j-1]
        if min1 <= max2 and min2 <= max1:
            if (len1+len2) % 2 == 0:
                print('inside')
                print(min1, min2)
                print(max1, max2)
                return (max(min1, min2)+min(max1, max2))/2
            else:
                return max(min1, min2)
        elif min1 > max2:
            right = i-1
        else:
            left = i+1


print(median_sorted_arr([10, 20, 30, 40, 50], [5, 15, 25, 35, 45]))
