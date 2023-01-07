class Solution:
    my_dict={}
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.my_dict={}
        def traversal(rt,tupl):
            if rt:
                if tupl[1] in self.my_dict:
                    self.my_dict[tupl[1]].append((tupl[0],rt.val))
                else:
                    self.my_dict[tupl[1]]=[(tupl[0],rt.val)]
                traversal(rt.left,[tupl[0]+1,tupl[1]-1])
                traversal(rt.right,[tupl[0]+1,tupl[1]+1])
            return
        traversal(root,[0,0])
        sorted_tuples=[]
        sorted_dict=sorted(self.my_dict.items())
        for item in sorted_dict:
            sorted_tuples.append(sorted(item[1]))
        res=[]
        for tuple in sorted_tuples:
            tmp=[]
            for item in tuple:
                tmp.append(item[1])
            res.append(tmp)
        return res