# import heapq

# def sort_k_sorted_arr(lst,k):
#     priority_q=[]
#     for i in range(k+1):
#         heapq.heappush(priority_q,lst[i])
#     index=0
#     print(priority_q[0])
#     for i in range(k+1,len(lst)):
#         lst[index]=heapq.heappop(priority_q)
#         index+=1
#         heapq.heappush(priority_q,lst[i])
#     while len(priority_q):
#         lst[index]=heapq.heappop(priority_q)
#         index+=1
#     return lst
from queue import PriorityQueue

def sort_k_sorted_arr(lst,k):
    priority_q=PriorityQueue()
    for i in range(k+1):
        priority_q.put(lst[i])
    index=0
    for i in range(k+1,len(lst)):
        lst[index]=priority_q.get()
        index+=1
        priority_q.put(lst[i])
    while priority_q.empty()==False:
        lst[index]=priority_q.get()
        index+=1
    return lst

print(sort_k_sorted_arr([9,8,7,19,18],2))