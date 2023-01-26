from queue import Queue
def bfs(adj_list,source,visited,indegree_dict):
    q=Queue()
    q.put(source)
    while q.empty()==False:
        curr=q.get()
        indegree_dict[curr]-=1
        if indegree_dict[curr]<=0:
            print('====',curr)
        if not visited[curr]:
            visited[curr]=True
            for vert in adj_list[curr]:
                q.put(vert)

def topological_sort(adj_list):
    indegree_dict=dict.fromkeys(range(len(adj_list)),0)
    for adj_nodes in adj_list:
        for node in adj_nodes:
            indegree_dict[node]=1+indegree_dict.get(node,0)
    visited=[False]*len(adj_list)
    for i in range(len(visited)):
        if visited[i]==False:
            bfs(adj_list,i,visited,indegree_dict)
    
topological_sort([[1,2],[3],[3],[4,5],[],[]])



