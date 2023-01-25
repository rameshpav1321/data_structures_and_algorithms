def dfs(adj_list,vert,visited):
    visited[vert]=True
    print(vert)
    for node in adj_list[vert]:
        if not visited[node]:
            dfs(adj_list,node,visited)

if __name__=="__main__":
    visited=[False]*5
    count=0
    for i in range(len(visited)):
        if not visited[i]:
            count+=1
            dfs([[1,2],[0,2],[0,1],[4],[3]],i,visited)
    print("count",count)
