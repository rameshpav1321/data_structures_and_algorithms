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
            if self.head.next!=self.head:
                while curr_node.next!=self.head:
                    curr_node=curr_node.next
            curr_node.next=new_node
            new_node.next=self.head
        else:
            self.head=Node(val)
            self.head.next=self.head