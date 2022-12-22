from binary_tree import Node

pre_index=0
def build_btree(inorder,preorder,in_start,in_end):
    global pre_index
    if in_start>in_end:
        return None
    root=Node(preorder[pre_index])
    print(root.data)
    pre_index+=1
    in_index=0
    for i in range(len(inorder)):
        if inorder[i]==root.data:
            in_index=i
    root.left=build_btree(inorder,preorder,in_start,in_index-1)
    root.right=build_btree(inorder,preorder,in_index+1,in_end)
    print(root.left.data)
    return root

print(build_btree([20,10,40,30,50],[10,20,30,40,50],0,4))