class Node:
    def __init__(self,val) -> None:
        self.data=val
        self.prev=None
        self.next=None

class DoublyLlist:
    def __init__(self) -> None:
        self.head=None

    def push_front(self,val):
        if self.head:
            new_node=Node(val)
            self.head.prev.next=new_node
            self.head.prev=new_node
            new_node.prev=self.head.prev
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=Node(val)
            self.head.next=self.head
            self.head.prev=self.head
    
    def push_back(self,val):
        if self.head:
            new_node=Node(val)
            self.head.prev.next=new_node
            self.head.prev=new_node
            new_node.prev=self.head.prev
            new_node.next=self.head
        else:
            self.head=Node(val)
            self.head.next=self.head
            self.head.prev=self.head