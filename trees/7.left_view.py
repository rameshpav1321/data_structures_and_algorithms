from binary_tree import btree
from queue import Queue

root=btree()

# def left_view(root):
#     q=Queue()
#     root.level=0
#     q.put(root)
#     res=[]
#     while q.empty()==False:
#         count=q.qsize()
#         for i in range(count):
#             ele=q.get()
#             if i==0:
#                 res.append(ele.data)
#                 print(res)
#             if ele.left:
#                 q.put(ele.left)
#             if ele.right:
#                  q.put(ele.right)
#     print(res)
max_level=0
def left_view(root,level):
    if root:
        global max_level
        if max_level<level:
            print(root.data,end=' ')
            max_level=level
        left_view(root.left,level+1)
        left_view(root.right,level+1)
left_view(root,1)