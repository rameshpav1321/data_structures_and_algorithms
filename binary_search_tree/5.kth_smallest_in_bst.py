class Solution:
    count=0
    res=-1
    def k_smallest(self,root,k,count):
        if root:
            self.k_smallest(root.left,k,self.count)
            self.count+=1
            if self.count==k:
                self.res=root.val
                return
            self.k_smallest(root.right,k,self.count)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest(root,k,0)
        return self.res