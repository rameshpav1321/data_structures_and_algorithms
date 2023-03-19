class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val>val:
                if root.left:
                    self.insertIntoBST(root.left,val)
                else:
                    root.left=TreeNode(val)
            else:
                if root.right:
                    self.insertIntoBST(root.right,val)
                else:
                    root.right=TreeNode(val)
            return root
        else:
            return TreeNode(val)