from binary_tree import btree

root=btree()

def children_sum(root):
    if root:
        if root.left==None and root.right==None:
            return True
        sum=0
        if root.left:
            sum+=root.left.data
        if root.right:
            sum+=root.right.data
        return root.data==sum and children_sum(root.left) and children_sum(root.right)

print(children_sum(root))