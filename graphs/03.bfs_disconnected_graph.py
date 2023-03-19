from queue import Queue
def bfs_disconnected(start):
    q=Queue()
    q.put(start)
    my_set=set()
    adj_list=[[1,2],[0,3],[0,3],[],[5,6],[4,6],[4,5]]
    prev,curr=start,start
    while q.empty()==False:
        curr=q.get()
        if curr==None:
                curr=prev+1
        if curr not in my_set:
                prev=curr
                my_set.add(curr)
                print(curr)
                for i in range(len(adj_list[curr])):
                    q.put(adj_list[curr][i])
    print(my_set)

bfs_disconnected(0)
#In the above implementation I assumed input adjacency list will have None as children for 
# disconnected node. 

# Or an alternate way is to maintain a shared boolean visited array and call bfs on each
# node that is not visited. Check count_islands_in_graph.py for this implementation.


