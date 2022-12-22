from binary_tree import btree
from queue import Queue

root=btree()

def spiral_traversal(root):
    q=Queue()
    q.put(root)
    temp_lst=[]
    ind=0
    while q.empty()==False:
        count=q.qsize()
        for i in range(count):
            ele=q.get()
            temp_lst.append(ele.data)
            if ele.left:
                q.put(ele.left)
            if ele.right:
                q.put(ele.right)
        for i in range(count):
            if ind%2==0:
                print(temp_lst.pop(0),end=' ')
            else:
                print(temp_lst.pop(),end=' ')
        ind+=1

spiral_traversal(root)

