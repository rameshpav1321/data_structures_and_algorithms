def stock_span(stocks):
    res=[1]
    stack=[0]
    for i in range(1,len(stocks)):
        while stack and stocks[stack[-1]]<=stocks[i]:
            stack.pop()
        res.append(i+1 if len(stack)==0 else i-stack[-1])
        stack.append(i)
    print(res)

stock_span([18,12,13,14,11,16])