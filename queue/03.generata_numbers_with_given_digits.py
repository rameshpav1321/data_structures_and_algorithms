def generate_numbers(nums,count):
    q=[]
    res=[]
    for num in nums:
        q.append(num)
    for i in range(count):
        val=q.pop(0)
        res.append(val)
        for num in nums:
            q.append(val+num)
    return res

print(generate_numbers(['5','6'],10))