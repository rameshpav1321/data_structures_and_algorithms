from queue import PriorityQueue

def max_items(lst,sum):
    count=0
    priority_q=PriorityQueue()
    for i in range(len(lst)):
        priority_q.put(lst[i])
    while priority_q.empty()==False:
        curr=priority_q.get()
        if sum-curr>=0:
            count+=1
            sum=sum-curr
    print(count)

max_items([20,33,45,10,456,5],35)
