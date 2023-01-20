from queue import Queue
def shortest_path(adj_list,source):
    my_set=set()
    q=Queue()
    dist=[0]*len(adj_list)
    q.put(source)
    my_set.add(source)
    while q.empty()==False:
        curr=q.get()
        for item in adj_list[curr]:
            if item not in my_set:
                dist[item]=dist[curr]+1
                my_set.add(item)
                q.put(item)
    print(dist)

shortest_path([[1,2],[0,2,3],[0,1,3],[2,1]],0)