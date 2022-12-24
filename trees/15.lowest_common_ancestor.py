from binary_tree import *

root=btree()

def lowest_common_ancestor(root,n1,n2):
    if root:
        if root.data==n1 or root.data==n2:
            return root
        left=lowest_common_ancestor(root.left,n1,n2)
        right=lowest_common_ancestor(root.right,n1,n2)
        if left!=None and right!=None:
            return root
        if left!=None:
            return left
        else:
            return right
    return None
        