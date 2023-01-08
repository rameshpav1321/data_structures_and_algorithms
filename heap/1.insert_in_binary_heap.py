def insert_heap(lst,ind):
    if ind==0:
        print(lst)
        return
    parent=(ind-1)//2
    if lst[parent]>lst[ind]:
        lst[parent],lst[ind]=lst[ind],lst[parent]
    insert_heap(lst,parent)

if __name__=="__main__":
    lst=[10,20,15,40,50,100,25,45]
    lst.append(12)
    ind=8
    insert_heap(lst,ind)