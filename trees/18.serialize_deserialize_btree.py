from queue import Queue
class Codec:
    def serialize(self, root):
        if root==None:return ''
        q=Queue()
        q.put(root)
        encode=[]
        while q.empty()==False:
            ele=q.get()
            if ele!=None:
                q.put(ele.left)
                q.put(ele.right)
                encode.append(str(ele.val))
            else:
                encode.append('None')
        return ' '.join(encode)
    def deserialize(self, data):
        if data=='': return None
        decode=data.split(' ')
        root=TreeNode(decode[0])
        q=Queue()
        q.put(root)
        i=1
        while q.empty()==False:
            ele=q.get()
            if decode[i]!='None':
                ele.left=TreeNode(int(decode[i]))
                q.put(ele.left)
            i+=1
            if decode[i]!='None':
                ele.right=TreeNode(int(decode[i]))
                q.put(ele.right)
            i+=1
        return root

# recursive solution
class Codec:
    def serialize(self, root):
        encode=[]
        def preorder(root):
            if root==None:
                encode.append('None')
                return
            encode.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ' '.join(encode)
           
    def deserialize(self, data):
        if data=='': return None
        decode=data.split(' ')
        self.i=0
        def preorder():
            if decode[self.i]!='None':
                root=TreeNode(int(decode[self.i]))
                self.i+=1
                root.left=preorder()
                root.right=preorder()
                return root
            else:
                self.i+=1
                return None
        return preorder()