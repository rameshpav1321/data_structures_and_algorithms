class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        self.level=None
def btree():
    # root=Node(10)
    # root.left=Node(15)
    # root.right=Node(20)
    # root.left.left=Node(30)
    # root.right.left=Node(40)
    # root.right.right=Node(50)
    # root.right.left.left=Node(60)
    # root.right.left.right=Node(70)
    root=Node(20)
    root.left=Node(8)
    root.right=Node(12)
    root.left.left=Node(3)
    root.left.right=Node(5)
    return root