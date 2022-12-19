from binary_tree import btree

root=btree()

def height(node):
    if node:
        left=height(node.left)
        right=height(node.right)
        return max(left,right)+1
    return 0

def balanced_tree(root):
    if root:
        lh=height(root.left)
        rh=height(root.right)
        return abs(lh-rh)<=1 and balanced_tree(root.left) and balanced_tree(root.right)
    return True

print(balanced_tree(root))    

def is_balanced(root):
    if root:
        lh=is_balanced(root.left)
        if lh==-1:
            return -1
        rh=is_balanced(root.right)
        if rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        else:
            return max(lh,rh)+1
    return 0
print(True if is_balanced(root)else False)     
