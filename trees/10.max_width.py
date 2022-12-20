from binary_tree import btree
from queue import Queue
root=btree()

def max_width(root):
    q=Queue()
    q.put(root)
    res=0
    while q.empty()==False:
        res=max(res,q.qsize())
        count=q.qsize()
        for i in range(count):
            ele=q.get()
            if ele.left:
                q.put(ele.left)
            if ele.right:
                q.put(ele.right)       
    return res

print(max_width(root))