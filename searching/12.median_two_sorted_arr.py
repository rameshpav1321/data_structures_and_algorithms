def median_sorted_arr(nums1, nums2):
    if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
    l1=len(nums1)
    l2=len(nums2)
    left,right=0,l1-1
    while left<=right:
        pt1=(left+right)//2
        pt2=(l1+l2)//2-pt1-2
        lmax1=float('-inf') if pt1<0 else nums1[pt1-1]
        rmin1=float('inf') if pt1==l1-1 else nums1[pt1]
        lmax2=float('-inf') if pt2<0 else nums2[pt2-1]
        rmin2=float('inf') if pt2==l2-1 else nums2[pt2]
        if lmax1<=rmin2 and lmax2<=rmin1:
            if (l1+l2)%2==0:
                return (max(lmax1,lmax2)+min(rmin1,rmin2))/2
            else:
                return max(lmax1,lmax2)
        elif lmax1>rmin2:
            right=pt1-1
        else:
            left=pt1+1
    


print(median_sorted_arr([10, 20], [30,40]))
