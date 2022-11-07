def function(nums,target):
    res=[-1,-1]
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        elif mid==0 or nums[mid]!=nums[mid-1]:
            res[0]=mid
            print(res)
            # else:
            #     res[1]=mid
            #     break
    return res




print(function([5,7,7,8,8,10],8))
