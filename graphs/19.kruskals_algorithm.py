def union(parent,rank,node1,node2):
    if rank[node1]<rank[node2]:
        parent[node1]=node2
    elif rank[node2]<rank[node1]:
        parent[node2]=node1
    else:
        parent[node2]=node1
        rank[node1]+=1

def find(parent,node):
    if parent[node]!=node:
        parent[node]=find(parent,parent[node])
    return parent[node]

def kruskals_algo(edj_lst,nodes):
    res=[[],[]]
    parent=[]
    rank=[]
    sorted_edges=sorted(edj_lst,key=lambda item:item[2])
    for node in range(nodes):
        parent.append(node)
        rank.append(0)
    while len(res[0])<nodes-1:
        u,v,w=sorted_edges.pop(0)
        x=find(parent,u)
        y=find(parent,v)
        if x!=y:
            res[0].append([u,v,w])
            res[1].append(w)
            union(parent,rank,x,y)
    res[1]=sum(res[1])
    print(res)

kruskals_algo([[0,1,10],[0,2,8],[1,2,5],[1,3,3],[2,3,4],[2,4,12],[3,4,15]],5)