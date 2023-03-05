def topo_sort(adj_lst,source,visited,stack):
    visited[source]=True
    for node in adj_lst[source]:
        if not visited[node]:
            topo_sort(adj_lst,node,visited,stack)
    stack.append(source)

def dfs(adj_lst_transpose,source,visited):
    visited[source]=True
    print(source)
    for node in adj_lst_transpose[source]:
        if not visited[node]:
            dfs(adj_lst_transpose,node,visited)


if __name__=="__main__":
    # adj_lst=[[1],[2,3],[0],[4],[]]
    adj_lst=[[1],[2,3],[],[0]]
    visited=[False]*len(adj_lst)
    topo_stack=[]
    for i in range(len(visited)):
        if not visited[i]:
            topo_sort(adj_lst,i,visited,topo_stack)

    adj_lst_transpose=[[] for i in range(len(adj_lst))]
    for i in range(len(adj_lst)):
        for j in adj_lst[i]:
            adj_lst_transpose[j].append(i)

    visited=[False]*len(adj_lst)
    for i in range(len(topo_stack)-1,-1,-1):
        if not visited[topo_stack[i]]:
            dfs(adj_lst_transpose,topo_stack[i],visited)
            print('==')


