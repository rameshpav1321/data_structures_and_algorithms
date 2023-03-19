class BinaryHeap:
    def __init__(self,lst):
        self.lst=lst
        self.size=len(lst)
    def left_child(self,i):
            return (2*i)+1 if (2*i)+1<len(self.lst) else -1
    def right_child(self,i):
        return (2*i)+2 if (2*i)+2<len(self.lst) else -1
    def parent(self,i):
            return -1 if i<1 else (i-1)//2
    def insert_heap(self,ind):
        if ind==0:
            return
        parent=(ind-1)//2
        if self.lst[parent]>self.lst[ind]:
            self.lst[parent],self.lst[ind]=self.lst[ind],self.lst[parent]
        self.insert_heap(parent)
    def min_heapify(self,index):
        left_child=self.left_child(index)
        right_child=self.right_child(index)
        min=index
        if left_child and self.lst[left_child]<self.lst[index]:
            min=left_child
        if right_child and self.lst[right_child]<self.lst[min]:
            min=right_child
        if min!=index:
            self.lst[min],self.lst[index]=self.lst[index],self.lst[min]
            self.min_heapify(min)
    def extract_min(self):
        self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
        res=self.lst.pop()
        self.min_heapify(0)
        return res
    def decrease_key(self,ind,key):
        self.lst[ind]=key
        self.insert_heap(ind)
    def delete_key(self,ind):
        self.lst[ind],self.lst[-1]=self.lst[-1],self.lst[ind]
        self.min_heapify(ind)
    def build_heap(self):
        for i in range(self.size-1,-1,-1):
            self.min_heapify(i)



    


test_heap=BinaryHeap([10,5,20,2,4,8])
test_heap.build_heap()
print(test_heap.lst)
