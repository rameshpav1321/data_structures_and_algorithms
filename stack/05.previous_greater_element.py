def previous_greater(lst):
    res=[-1]
    stack=[lst[0]]
    for i in range(1,len(lst)):
        while stack and stack[-1]<lst[i]:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(lst[i])
    print(res)

previous_greater([20,30,10,5,15])