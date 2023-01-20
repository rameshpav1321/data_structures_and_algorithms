def add_edge(adj_lst,u,v):
    adj_lst[u].append(v)
    adj_lst[v].append(u)



def adjacency_list(lst,vert):
    adj_list=[[] for i in range(vert)]
    add_edge(adj_list, 0, 1); 
    add_edge(adj_list, 0, 2); 
    add_edge(adj_list, 1, 2); 
    add_edge(adj_list, 1, 3); 
    return adj_list

adjacency_list([0,1,2,3,4],5)