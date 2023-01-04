class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val==key:
                if root.right==None:
                    return root.left
                elif root.left==None:
                    return root.right
                else:
                    curr=root.right
                    while curr.left:
                        curr=curr.left
                    root.val=curr.val
                    root.right=self.deleteNode(root.right,curr.val)
            elif root.val<key:
                root.right= self.deleteNode(root.right,key)
            else:
                root.left=self.deleteNode(root.left,key)
            return root
        return None