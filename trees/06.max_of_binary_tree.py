from queue import Queue
class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
root.right.left.left=Node(60)
root.right.left.right=Node(70)

def max_of_tree(root):
    q=Queue()
    q.put(root)
    max_ele=0
    while q.empty()==False:
        ele=q.get()
        max_ele=max(max_ele,ele.data)
        if ele.left:
            q.put(ele.left)
        if ele.right:
            q.put(ele.right)
    print("Max node in the tree:",max_ele)

max_of_tree(root)