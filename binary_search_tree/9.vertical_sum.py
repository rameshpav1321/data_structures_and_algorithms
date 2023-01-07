class Solution:
    my_dict={}
    def verticalSum(self, root):
        self.my_dict={}
        def preorder(rt,i):
            if rt:
                self.my_dict[i]=rt.data+self.my_dict.get(i,0)
                preorder(rt.left,i-1)
                preorder(rt.right,i+1)
            return
        preorder(root,0)
        res=[]
        sorted_keys=sorted(self.my_dict)
        for key in sorted_keys:
            res.append(self.my_dict[key])
        return res