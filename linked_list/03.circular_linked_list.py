class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class CircularLlist:
    def __init__(self) -> None:
        self.head=None

    def traverse(self):
        if self.head:
            if self.head.next==self.head:
                print(self.head.data)
            else:
                curr_node=self.head
                while curr_node.next!=self.head:
                    print(curr_node.data)
                    curr_node=curr_node.next
                print(curr_node.data)
        else:
            return
    def insert_end(self,val):
        if self.head:
            new_node=Node(val)
            curr_node=self.head
            if curr_node.next!=self.head:
                while curr_node.next!=self.head:
                    curr_node=curr_node.next
            curr_node.next=new_node
            new_node.next=self.head
        else:
            self.head=Node(val)
            self.head.next=self.head
    def insert_begin(self,val):
        if self.head:
            new_node=Node(val)
            new_node.next=self.head.next
            self.head.next=new_node
            self.head.data,self.head.next.data=self.head.next.data,self.head.data
            # new_node=Node(val)
            # curr_node=self.head
            # if curr_node.next!=self.head:
            #     while curr_node.next!=self.head:
            #         curr_node=curr_node.next
            # curr_node.next=new_node
            # new_node.next=self.head
            # self.head=new_node
        else:
            self.head=Node(val)
            self.head.next=self.head
    def delete_head(self):
        if self.head:
            if self.head.next==self.head:
                self.head=None
            else:
                self.head.data,self.head.next.data=self.head.next.data,self.head.data
                self.head.next=self.head.next.next
    def delete_k_node(self,k):
        if self.head:
            if k==1:
                self.delete_head()
            else:
                count=1
                curr_node=self.head
                temp=self.head
                while count!=k:
                    temp=curr_node
                    curr_node=curr_node.next
                    count+=1
                temp.next=curr_node.next

circ_llist=CircularLlist()
circ_llist.insert_begin(10)
circ_llist.insert_end(20)
circ_llist.insert_end(30)
circ_llist.head.next.next.next=circ_llist.head
circ_llist.insert_begin(15)
circ_llist.delete_k_node(5)
circ_llist.traverse()