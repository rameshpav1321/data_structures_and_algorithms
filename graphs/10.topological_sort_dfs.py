def dfs(adj_list,source,visited,stack):
    visited[source]=True
    for vert in adj_list[source]:
        if not visited[vert]:
            dfs(adj_list,vert,visited,stack)
    stack.append(source)

def topological_sort(adj_list):
    visited=[False]*len(adj_list)
    stack=[]
    for i in range(len(visited)):
        if not visited[i]:
            dfs(adj_list,i,visited,stack)
    print(stack)