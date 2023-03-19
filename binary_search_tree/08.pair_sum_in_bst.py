class Solution:
    my_set=set()
    res=False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.my_set=set()
        def inorder(rt,tr):
            if rt:
                inorder(rt.left,tr)
                if tr-rt.val in self.my_set:
                    self.res=True
                else:
                    self.my_set.add(rt.val)
                inorder(rt.right,tr)
        inorder(root,k)
        return self.res