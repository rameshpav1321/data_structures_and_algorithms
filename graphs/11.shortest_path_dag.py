def dfs(adj_list,start,visited,dist_dict):
    visited[start]=True
    for tupl in adj_list[start]:
        if dist_dict[start]+tupl[1]<dist_dict[tupl[0]]:
            dist_dict[tupl[0]]=dist_dict[start]+tupl[1]
        dfs(adj_list,tupl[0],visited,dist_dict)


def shortest_path_dag(adj_list,source):
    visited=[False]*len(adj_list)
    dist_dict=dict.fromkeys(range(len(adj_list)),float('inf'))
    dist_dict[source]=0
    dfs(adj_list,source,visited,dist_dict)
    print(dist_dict)

# shortest_path_dag([[(1,1)],[(2,3),(3,2)],[(3,4)],[]],2)
shortest_path_dag([[(1,2)],[(2,3)],[(3,6)],[],[(2,2),(0,1),(5,4)],[(3,1)]],4)