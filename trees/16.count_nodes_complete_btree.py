from binary_tree import *

root=btree()

def count_nodes(root):
    lh,rh=0,0
    curr=root
    while curr:
        lh+=1
        curr=curr.left
    curr=root
    while curr:
        rh+=1
        curr=curr.right
    if lh==rh:
        return 2**lh-1
    return 1+count_nodes(root.left)+count_nodes(root.right)

print(count_nodes(root))