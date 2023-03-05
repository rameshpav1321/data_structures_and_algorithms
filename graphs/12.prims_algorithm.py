# minimum spanning tree
def prims_algo(adj_matrix):
    vertices=len(adj_matrix)
    key=[float('inf')]*vertices
    key[0]=res=0
    mst=[False]*vertices
    for i in range(vertices):
        u=-1
        for j in range(vertices):
            if not mst[u] and (u==-1 or key[j]<key[u]):
                u=i
        mst[u]=True
        res+=key[u]
        for v in range(vertices):
            if adj_matrix[u][v]!=0 and not mst[v]:
                key[v]=min(key[v],adj_matrix[u][v])
    return res