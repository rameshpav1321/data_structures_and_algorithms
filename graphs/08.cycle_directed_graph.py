def dfs(adj_list,source,visited,rec_stack):
    visited[source]=True
    rec_stack[source]=True
    for vert in adj_list[source]:
        if not visited[vert] and dfs(adj_list,vert,visited,rec_stack):
            return True
        elif rec_stack[vert]:
            return True
    rec_stack[source]=False
    return False

def detect_cycle(adj_list):
    visited=[False]*len(adj_list)
    rec_stack=[False]*len(adj_list)
    for i in range(len(visited)):
        if not visited[i]:
            if dfs(adj_list,i,visited,rec_stack):
                return True
    return False
