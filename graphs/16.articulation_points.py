def articulation_points(adj_lst,source,visited,disc,low,parent,art_points,time):
    visited[source]=True
    children=0
    time+=1
    disc[source]=low[source]=time
    for node in adj_lst[source]:
        if not visited[node]:
            parent[node]=source
            children+=1
            articulation_points(adj_lst,node,visited,disc,low,parent,art_points,time)
            low[source]=min(low[source],low[node])
            if parent[source]==None and children>1:
                art_points[source]=True
            if parent[source]!=None and low[node]>=disc[source]:
                art_points[source]=True
        elif node!=parent[source]:
            low[source]=min(low[source],disc[node])

if __name__=="__main__":
    # adj_lst=[[1,2,3],[0,2],[0,1],[0,4],[3]]
    adj_lst=[[1],[0,2],[1,3],[2]]
    visited=[False]*len(adj_lst)
    disc=[0]*len(adj_lst)
    low=[0]*len(adj_lst)
    art_points=[False]*len(adj_lst)
    parent=[None]*len(adj_lst)
    for i in range(len(adj_lst)):
        if not visited[i]:
            articulation_points(adj_lst,i,visited,disc,low,parent,art_points,0)
    for i in range(len(art_points)):
        if art_points[i]:
            print(i)