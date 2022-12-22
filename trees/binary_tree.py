class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        self.level=None
def btree():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.left.left=Node(8)
    root.left.left.right=Node(9)
    root.right.left.left=Node(10)
    
    return root