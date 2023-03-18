def tarjans_algorithm(adj_lst,source,disc,low,stack,is_stack_member,time):
    stack.append(source)
    is_stack_member.add(source)
    time+=1
    disc[source]=low[source]=time
    for node in adj_lst[source]:
        if disc[node]==-1:
            tarjans_algorithm(adj_lst,node,disc,low,stack,is_stack_member,time)
            low[source]=min(low[source],low[node])
        elif node in is_stack_member:
            low[source]=min(low[source],disc[node])
    w = -1  # To store stack extracted vertices
    if low[source] == disc[source]:
        while w != source:
            w = stack.pop()
            print(w, end=" ")
            is_stack_member.remove(w)

        print()

if __name__=="__main__":
    adj_lst=[[2,3],[0],[1],[4],[]]
    disc=[-1]*len(adj_lst)
    low=[-1]*len(adj_lst)
    stack=[]
    is_stack_member=set()
    for i in range(len(adj_lst)):
        if disc[i]==-1:
            tarjans_algorithm(adj_lst,i,disc,low,stack,is_stack_member,0)
    
