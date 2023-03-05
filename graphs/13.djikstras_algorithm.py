from queue import Queue
def djikstras_algo(adj_lst,source):
    visited=[False]*len(adj_lst)
    dist=[float('inf')]*len(adj_lst)
    dist[source]=0
    min_heap=Queue()
    min_heap.put([0,source])
    while min_heap.empty()==False:
        distance,vert=min_heap.get()
        dist[vert]=distance
        visited[vert]=True
        for tupl in adj_lst[vert]:
            if not visited[tupl[0]] and dist[vert]+tupl[1]<dist[tupl[0]]:
                dist[tupl[0]]=dist[vert]+tupl[1]
                min_heap.put([dist[tupl[0]],tupl[0]])
    print(dist)

if __name__=="__main__":
    graph=[[0,5,10,0],[5,0,3,20],[10,3,0,2],[0,20,2,0]]
    adj_lst=[[] for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]!=0:
                adj_lst[i].append((j,graph[i][j]))
    djikstras_algo(adj_lst,0)
