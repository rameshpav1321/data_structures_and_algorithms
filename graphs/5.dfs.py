def dfs(adj_list,vert,visited):
    if visited[vert]:
        return
    visited[vert]=True
    print(vert)
    for i in range(len(adj_list[vert])):
        dfs(adj_list,adj_list[vert][i],visited)

if __name__=="__main__":
    visited=[False]*5
    count=0
    for i in range(len(visited)):
        if not visited[i]:
            count+=1
            dfs([[1,2],[0,2],[0,1],[4],[3]],i,visited)
    print("count",count)
