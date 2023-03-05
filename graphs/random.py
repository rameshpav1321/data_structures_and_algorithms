from queue import Queue
class Solution:
    def djikstras(self,adj_lst,source):
        min_heap=Queue()
        visited=[False]*len(adj_lst)
        res_dict={i:[float('inf'),float('inf')] for i in range(len(adj_lst))}
        res_dict[source]=[0,0]
        min_heap.put([0,0,0])
        while min_heap.empty()==False:
            cost,node,dist=min_heap.get()
            res_dict[node]=[cost,dist]
            visited[node]=True
            for tupl in adj_lst[node]:
                if not visited[tupl[0]] and res_dict[node][0]+tupl[1]<res_dict[tupl[0]][0]:
                    res_dict[tupl[0]][0]=res_dict[node][0]+tupl[1]
                    res_dict[tupl[0]][1]=res_dict[node][1]+1
                    min_heap.put([res_dict[tupl[0]][0],tupl[0],res_dict[tupl[0]][1]])
        print(res_dict)


    def findCheapest(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_lst=[[] for i in range(n)]
        for edge in flights:
            adj_lst[edge[0]].append([edge[1],edge[2]])
        print(adj_lst)
        self.djikstras(adj_lst,src)
        return 0