from queue import PriorityQueue
def k_closest_elements(lst,k,x):
    priority_q=PriorityQueue()
    for item in lst:
        priority_q.put((abs(item-x),item))
    res=[]
    while priority_q.empty()==False:
        curr=priority_q.get()
        if len(res)!=k:
            res.append(curr[1])
    print(res)
    
k_closest_elements([10,5,7,3,4],2,8)