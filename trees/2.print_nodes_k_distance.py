class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node(70)

def print_nodes(root,k):
    if root:
        if k==0:
            print(root.data)
            return
        print_nodes(root.left,k-1)
        print_nodes(root.right,k-1)

print_nodes(root,2)

