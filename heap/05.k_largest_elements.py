from queue import PriorityQueue

def k_largest_elements(lst,k):
    priority_q=PriorityQueue()
    for i in range(k):
        priority_q.put(lst[i])
    for i in range(k,len(lst)):
        curr=priority_q.get()
        if lst[i]<curr:
            priority_q.put(curr)
        else:
            priority_q.put(lst[i])
    for i in range(priority_q.qsize()):
        print(priority_q.get())

k_largest_elements([5,10,15,20,8,25,18],3)