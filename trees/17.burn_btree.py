from binary_tree import btree

root=btree()

class Dist:
    def __init__(self,val):
        self.dist=val
res=0
def burn_btree(root,leaf,dist):
    global res
    if root:
        if root.data==leaf:
            dist.dist=0
            return 1
        ldist=Dist(-1)
        rdist=Dist(-1)
        lh=burn_btree(root.left,leaf,ldist)
        rh=burn_btree(root.right,leaf,rdist)
        if ldist.dist!=-1:
            dist.dist=ldist.dist+1
            res=max(res,dist.dist+rh)
        if rdist.dist!=-1:
            dist.dist=rdist.dist+1
            res=max(res,dist.dist+lh)
        return max(lh,rh)+1
    return 0

dist=Dist(-1)
burn_btree(root,9,dist)
print(res)
