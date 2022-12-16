class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        self.level=None

root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
root.right.left.left=Node(60)
root.right.left.right=Node(70)

def level_order_line(root):
    queue=[]
    root.level=0
    queue.append(root)
    prev=root.level
    while len(queue):
        ele=queue.pop(0)
        if prev!=ele.level:
            prev=ele.level
            print()
        print(ele.data,end=" ")
        if ele.left:
            ele.left.level=prev+1
            queue.append(ele.left)
        if ele.right:
            ele.right.level=prev+1
            queue.append(ele.right)

level_order_line(root)
