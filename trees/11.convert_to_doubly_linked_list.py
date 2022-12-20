from binary_tree import *

root=btree()
prevNode=None
head=None
def convert_llist(root):
    global prevNode
    global head
    if root==None:
        return root
    convert_llist(root.left)
    if prevNode==None:
        head=root
    else:
        prevNode.right=root
        root.left=prevNode
    prevNode=root
    convert_llist(root.right)
    return head

l=convert_llist(root)
print(l.data)
