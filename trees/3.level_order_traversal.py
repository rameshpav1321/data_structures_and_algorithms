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

def level_order_traversal(root):
    queue=[]
    queue.append(root)
    while len(queue):
        ele=queue.pop(0)
        print(ele.data,end=" ")
        if ele.left:
            queue.append(ele.left)
        if ele.right:
            queue.append(ele.right)

level_order_traversal(root)