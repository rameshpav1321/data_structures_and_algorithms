class Solution:
    def floor(self, root, x):
        # Code here
        res=-1
        while root:
            if root.data==x:
                return root.data
            elif root.data>x:
                root=root.left
            else:
                res=root.data
                root=root.right
        return res