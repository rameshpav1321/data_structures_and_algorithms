def bellman_ford_algo(adj_lst):
    dist=[float('inf')]*len(adj_lst)
    dist[0]=0
    for i in range(len(adj_lst)-1):
        for start_node in range(len(adj_lst)):
            for tupl in adj_lst[start_node]:
                if dist[tupl[0]]>dist[start_node]+tupl[1]:
                    dist[tupl[0]]=dist[start_node]+tupl[1]
    print(dist)


if __name__=="__main__":
    graph=[[0,5,10,0],[5,0,3,20],[10,3,0,2],[0,20,2,0]]
    adj_lst=[[] for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]!=0:
                adj_lst[i].append((j,graph[i][j]))
    bellman_ford_algo(adj_lst)