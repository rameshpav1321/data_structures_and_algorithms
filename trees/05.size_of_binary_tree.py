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

def size(root):
    if root:
        left=size(root.left)
        right=size(root.right)
        return left+right+1
    else:
        return 0

print(size(root))