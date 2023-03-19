from queue import Queue
def bfs(start):
    q=Queue()
    my_set=set()
    adj_lst=[[1,2],[0],[0,3,4],[2],[2]]
    q.put(start)
    while q.empty()==False:
        curr=q.get()
        if curr not in my_set:
            print(curr)
            my_set.add(curr)
            for i in range(len(adj_lst[curr])):
                q.put(adj_lst[curr][i])
    print(my_set)
        
bfs(2)

        


    

