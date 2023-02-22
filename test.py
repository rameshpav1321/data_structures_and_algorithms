from queue import Queue
def shortest_path(adj_list,source):
    my_set=set()
    q=Queue()
    q.put(source,0)
    res=[]
    while q.empty()==False:
        curr,dist=q.get()
        res.append(dist)
        if curr not in my_set:
            for i in range(len(adj_list[curr])):
                q.put((adj_list[curr][i],dist+1))
    print(res)
shortest_path([[1,2],[0,2,3],[0,1,3],[1,2]],0)