class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val==val:
               return root
            elif root.val<val:
                return self.searchBST(root.right,val)
            else:
                return self.searchBST(root.left,val)
        return None  


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val==val:
                return root
            elif root.val<val:
                root=root.right
            else:
                root=root.left
        return None