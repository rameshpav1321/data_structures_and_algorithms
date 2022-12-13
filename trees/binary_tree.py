class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)   
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def height(root):
    if root:
        left=height(root.left)
        right=height(root.right)
        return max(left,right)+1
    return 0

root=Node(10)
root.left=Node(9)
root.right=Node(8)
root.left.left=Node(7) 
root.left.right=Node(6)
print("\nInorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nHeight of the tree:",height(root))

        