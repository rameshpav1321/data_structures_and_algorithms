from queue import Queue
def bfs(adj_lst,start,visited):
    visited[start]=True
    q=Queue()
    q.put(start)
    while q.empty()==False:
        curr=q.get()
        if not visited[curr]:
            print(curr)
            visited[curr]=True
            for i in range(len(adj_lst[curr])):
                q.put(adj_lst[curr][i])

def count_islands(adj_li,vert):
    visited=[False]*vert
    count=0
    for i in range(len(visited)):
        if visited[i]==False:
            count+=1
            bfs(adj_li,i,visited)
    return count

count_islands([[1,2],[0,3],[0,3],[],[5,6],[4,6],[4,5]],7)

