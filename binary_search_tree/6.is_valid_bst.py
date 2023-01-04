class Solution:
    prev=float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if self.isValidBST(root.left)==False:
                return False
            if root.val<=self.prev:
                return False
            self.prev=root.val
            return self.isValidBST(root.right)
        return True