from binary_tree import btree
root=btree()
count=0
def diameter(root):
    global count
    if root:
        left=diameter(root.left)
        right=diameter(root.right)
        count=max(count,left+right+1)
        return max(left,right)+1
    return 0