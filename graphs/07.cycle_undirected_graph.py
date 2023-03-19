def dfs(adj_list,source,visited,parent):
    visited[source]=True
    for vert in adj_list[source]:
        if not visited[vert]:
            if dfs(adj_list,vert,visited,source):
                return True
        elif parent!=vert:
            return True
    return False

def detect_cycle(adj_list):
    visited=[False]*5
    for i in range(len(visited)):
        if not visited[i]:
            if dfs(adj_list,i,visited,-1):
                return True
    return False