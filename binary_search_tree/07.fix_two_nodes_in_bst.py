class Solution:
    first,second,prev=None,None,None
    def recoverTree(self, rt: Optional[TreeNode]) -> None:
        def fix_bst(root):
            if root:
                fix_bst(root.left)
                if self.prev and root.val<=self.prev.val:
                    if self.first==None:
                        self.first=self.prev
                    self.second=root
                self.prev=root
                fix_bst(root.right)
        fix_bst(rt)
        self.first.val,self.second.val=self.second.val,self.first.val